# This Python file uses the following encoding: utf-8
import os
import sys

from PySide6.QtCore import QDir
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog

import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np
from sklearn.metrics import r2_score
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_Main_Window

class Main_Window(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Main_Window()
        self.ui.setupUi(self)

        self.connect_interface()

    def connect_interface(self):

        self.ui.browseButton.clicked.connect(self.browse_file)

    def browse_file(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly

        file_name, _ = QFileDialog.getOpenFileName(self, 'Select a .db file', os.path.dirname(os.path.abspath(__file__))+"/Databases", 'SQLite Database Files (*.db);;All Files (*)', options=options)

        if file_name:
            self.connect_to_database(file_name)

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


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Main_Window()
    widget.show()
    sys.exit(app.exec())
