# This Python file uses the following encoding: utf-8
import os
import sys

from PySide6.QtCore import QDir
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog, QVBoxLayout


import sqlite3
import pandas as pd
from scipy.optimize import curve_fit
import numpy as np
from sklearn.metrics import r2_score
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from scipy.signal import argrelextrema
import random

#import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_Main_Window


# External Function :

def choose_best_regression(x, y):
    # Define the models
    def linear_func(x, a, b):
        return a * x + b

    def exponential_func(x, a, b, c):
        return a * np.exp(b * x) + c



    # Fit the linear model
    popt_linear, _ = curve_fit(linear_func, x, y)
    y_pred_linear = linear_func(x, *popt_linear)
    r2_linear = r2_score(y, y_pred_linear)



    # Fit the exponential model
    try:
        popt_exponential, _ = curve_fit(exponential_func, x, y)
        y_pred_exponential = exponential_func(x, *popt_exponential)
        r2_exponential = r2_score(y, y_pred_exponential)
    except:
        r2_exponential = -np.inf

    # Compare R-squared values
    if r2_linear > r2_exponential:
        return 'Linear Regression', popt_linear, r2_linear, y_pred_linear
    else:
        return 'Exponential Regression', popt_exponential, r2_exponential, y_pred_exponential




def simulate_hourly_problems_linear(hour, a, b):
    probability = a * hour + b
    if random.random() < probability:
        return 1
    else:
        return 0

def simulate_hourly_problems_exponential(hour, a, b, c):
    probability = a * np.exp(b * hour) + c
    if random.random() < probability:
        return 1
    else:
        return 0

def simulate_hours_to_failure(threshold, probability_accept, regression_type, regression_params):
    # Simulate hours until failure
    total_problems = 0
    hours = 1000  # You can adjust the number of hours to simulate

    for hour in range(hours):
        if regression_type == 'Linear Regression':
            probability_failure = simulate_hourly_problems_linear(hour, *regression_params)
        elif regression_type == 'Exponential Regression':
            probability_failure = simulate_hourly_problems_exponential(hour, *regression_params)
        else:
            raise ValueError("Invalid regression type")

        total_problems += probability_failure

    # Check if the part needs to be changed
    if total_problems > threshold:
        print("The part needs to be changed.")
    else:
        print("The part does not need to be changed at this time.")


# QT INTERFACE :

class Main_Window(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Main_Window()
        self.ui.setupUi(self)

        self.connect_interface()

    def connect_interface(self):

        self.ui.browseButton.clicked.connect(self.browse_file)

        # Set up the matplotlib figure and canvas
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        self.ui.plotWidget.setLayout(QVBoxLayout())
        self.ui.plotWidget.layout().addWidget(self.canvas)

        self.figure2 = Figure()
        self.canvas2 = FigureCanvas(self.figure2)
        self.ui.plotWidget_hist.setLayout(QVBoxLayout())
        self.ui.plotWidget_hist.layout().addWidget(self.canvas2)

        self.figure3 = Figure()
        self.canvas3 = FigureCanvas(self.figure3)
        self.ui.plotWidget_hist2.setLayout(QVBoxLayout())
        self.ui.plotWidget_hist2.layout().addWidget(self.canvas3)

    def browse_file(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly

        file_name, _ = QFileDialog.getOpenFileName(self, 'Select a .db file', os.path.dirname(os.path.abspath(__file__))+"/Databases", 'SQLite Database Files (*.db);;All Files (*)', options=options)

        if file_name:
            #info = self.get_database_info(file_name)
            #print(info["Error"])
            #print(info["Size"])
            self.ui.fileName.setText(file_name.split("Databases/")[1])
            self.get_linear_regression(file_name)
            self.get_occurency(file_name)

    def get_database_info(self, db_file):
            try:
                file_size = os.path.getsize(db_file)
                conn = sqlite3.connect(db_file)
                cursor = conn.cursor()

                cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
                table_names = [table[0] for table in cursor.fetchall()]

                table_info = {}
                for table_name in table_names:
                    cursor.execute(f"PRAGMA table_info({table_name});")
                    columns = cursor.fetchall()
                    num_columns = len(columns)

                    cursor.execute(f"SELECT COUNT(*) FROM {table_name};")
                    num_rows = cursor.fetchone()[0]

                    table_info[table_name] = {"rows": num_rows, "columns": num_columns}

                conn.close()
                return {"Size": file_size, "Tables": table_names, "Info": table_info}
            except Exception as e:
                return {"Error": str(e)}

    def get_table_name(self, file_name):
        try:
            conn = sqlite3.connect(file_name)
            cursor = conn.cursor()

            # Query to retrieve the name of all tables in the database
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")

            # Fetch the result (table names)
            table_names = cursor.fetchall()

            # Extract table names from the result
            table_names = [table[0] for table in table_names]

            conn.close()

            if table_names:
                return table_names
            else:
                return "No tables found in the database."
        except sqlite3.Error as e:
            return "Error connecting to the database: " + str(e)


    def connect_to_database(self, file_name):
        try:
            conn = sqlite3.connect(file_name)
            print("Connected to the database:", file_name)

            cursor = conn.cursor()

            table_names = self.get_table_name(file_name)

            for table in table_names:

                cursor.execute("SELECT * FROM " + table)

                # Fetch all rows and column names
                rows = cursor.fetchall()
                column_names = [description[0] for description in cursor.description]

                # Print column names
                print("Column Names:", column_names)

                # Print all rows
                for row in rows:
                    print(row)

                conn.close()


        except sqlite3.Error as e:
            print("Error connecting to the database:", e)


    def get_occurency(self, file_name):
        conn = sqlite3.connect(file_name)

        # Query to extract data for occurrences
        query_occurrences = "SELECT FH, COUNT(*) as num_occurrences FROM Occurrences GROUP BY FH"
        df = pd.read_sql_query(query_occurrences, conn)

        # Query to extract data for occurrences that led to part replacement
        query_occurrences_repl = "SELECT FH, COUNT(*) as num_occurrences FROM Occurrences WHERE Troubleshootingréalisé = 'part replacement' GROUP BY FH"
        df2 = pd.read_sql_query(query_occurrences_repl, conn)

        # Creating intervals of 5000 flight hours
        df['FH_interval'] = (df['FH'] // 5000) * 5000
        interval_data = df.groupby('FH_interval')['num_occurrences'].sum().reset_index()
        interval_data['cumulative_occurrences'] = interval_data['num_occurrences'].cumsum()

        df2['FH_interval'] = (df2['FH'] // 5000) * 5000
        interval_data_rep = df2.groupby('FH_interval')['num_occurrences'].sum().reset_index()
        interval_data_rep['cumulative_occurrences'] = interval_data_rep['num_occurrences'].cumsum()

        # Linear regression model
        mid_points = interval_data['FH_interval'] + 2500
        choice, popt, r2, y_pred = choose_best_regression(mid_points, interval_data['cumulative_occurrences'])

        # Find local maxima
        occurrences_array = interval_data['num_occurrences'].values
        local_max_indices = argrelextrema(occurrences_array, np.greater)[0]
        local_max_intervals = interval_data['FH_interval'].iloc[local_max_indices]

        occurrences_rep_array = interval_data_rep['num_occurrences'].values
        local_max_indices_rep = argrelextrema(occurrences_rep_array, np.greater)[0]
        local_max_intervals_rep = interval_data_rep['FH_interval'].iloc[local_max_indices_rep]

        # Plotting
        # Clear the existing figure
        self.figure2.clear()
        self.figure3.clear()

        # Create two subplots (axes) on the figure
        ax1 = self.figure2.add_subplot(111)
        ax2 = self.figure3.add_subplot(111)

        # Create interval labels for both datasets
        interval_labels = [f'{int(interval)}-{int(interval) + 5000}' for interval in interval_data['FH_interval']]
        interval_labels2 = [f'{int(interval)}-{int(interval) + 5000}' for interval in interval_data_rep['FH_interval']]

        # Plot the first bar chart
        ax1.bar(interval_labels, interval_data['num_occurrences'], color='green')
        ax1.set_xlabel('Total Flight Hours Interval')
        ax1.set_ylabel('Number of Occurrences')
        ax1.set_title('Occurrences in Each 5000 Flight Hours Interval')
        ax1.set_xticklabels(interval_labels, rotation=45, ha='right')

        # Plot the second bar chart
        ax2.bar(interval_labels2, interval_data_rep['num_occurrences'], color='red')
        ax2.set_xlabel('Total Flight Hours Interval')
        ax2.set_ylabel('Number of Occurrences that led to a replacement of the part')
        ax2.set_title('Occurrences in Each 5000 Flight Hours Interval')
        ax2.set_xticklabels(interval_labels2, rotation=45, ha='right')

        # Annotate local maxima on the second plot
        for idx in local_max_indices_rep:
            ax2.annotate('Max', xy=(interval_labels2[idx], occurrences_rep_array[idx]),
                         xytext=(0, 10), textcoords="offset points",
                         ha='center', va='bottom', arrowprops=dict(facecolor='black', shrink=0.05))

        self.figure2.tight_layout()
        self.figure3.tight_layout()

        # Redraw the canvas with the new plots
        self.canvas2.draw()
        self.canvas3.draw()


        # Print out the intervals that are local maxima
        print("Flight hours intervals that are local maximums (Occurrences):", local_max_intervals.tolist())
        print("Flight hours intervals that are local maximums (Occurrences with part replacement):", local_max_intervals_rep.tolist())

    def get_linear_regression(self, file_name):
        conn = sqlite3.connect(file_name)

        # Query to extract data for occurrences
        query_occurrences = "SELECT FH, COUNT(*) as num_occurrences FROM Occurrences GROUP BY FH"
        df = pd.read_sql_query(query_occurrences, conn)

        # You can set your threshold value
        threshold = 1000
        probability_accept = 0.9  # Set your acceptable probability here

        # Extract x and y values for regression
        x = df['FH'].values
        y = df['num_occurrences'].values
        print(y)
        print("\n len x", len(x))
        print("\n len y", len(y))

        somme_occur=[0]

        for i in range(len(y)-1):
            somme_occur.append(somme_occur[i]+ y[i])
        print(somme_occur)
        print("\n len occur", len(somme_occur))


        # Choose the best regression model
        regression_type, regression_params, r2, y_pred = choose_best_regression(x, somme_occur)

        # Print the chosen regression model and its parameters
        print(f"Chosen Regression Model: {regression_type}")
        print(f"Regression Parameters: {regression_params}")
        print(f"R-squared: {r2}")

        # Simulate hours until failure based on the chosen regression model
        simulate_hours_to_failure(threshold, probability_accept, regression_type, regression_params)

        ax = self.figure.add_subplot(111)
        ax.clear()  # Clear existing data/plots
        ax.scatter(x, somme_occur)
        ax.plot(x, y_pred)

        # Update the canvas
        self.figure.tight_layout()
        self.canvas.draw()

        # Close database connection
        conn.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Main_Window()
    widget.show()
    sys.exit(app.exec())
