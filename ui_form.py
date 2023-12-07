# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.2.4
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFormLayout, QFrame,
    QGridLayout, QHBoxLayout, QLabel, QMainWindow,
    QMenuBar, QPushButton, QScrollArea, QSizePolicy,
    QStatusBar, QTabWidget, QToolBox, QVBoxLayout,
    QWidget)

class Ui_Main_Window(object):
    def setupUi(self, Main_Window):
        if not Main_Window.objectName():
            Main_Window.setObjectName(u"Main_Window")
        Main_Window.resize(1176, 754)
        icon = QIcon()
        icon.addFile(u"Icon.png", QSize(), QIcon.Normal, QIcon.Off)
        Main_Window.setWindowIcon(icon)
        self.centralwidget = QWidget(Main_Window)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(360, 16777215))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.scrollArea = QScrollArea(self.frame)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 338, 670))
        self.verticalLayout_3 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.toolBox = QToolBox(self.scrollAreaWidgetContents)
        self.toolBox.setObjectName(u"toolBox")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.page.setGeometry(QRect(0, 0, 320, 559))
        self.horizontalLayout_3 = QHBoxLayout(self.page)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.frame_3 = QFrame(self.page)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMaximumSize(QSize(16777215, 16777215))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_7 = QFrame(self.frame_3)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMaximumSize(QSize(16777215, 50))
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.formLayout = QFormLayout(self.frame_7)
        self.formLayout.setObjectName(u"formLayout")
        self.fileName = QLabel(self.frame_7)
        self.fileName.setObjectName(u"fileName")
        self.fileName.setMinimumSize(QSize(150, 0))

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.fileName)

        self.browseButton = QPushButton(self.frame_7)
        self.browseButton.setObjectName(u"browseButton")
        self.browseButton.setMaximumSize(QSize(100, 16777215))
        icon1 = QIcon()
        iconThemeName = u"folder"
        if QIcon.hasThemeIcon(iconThemeName):
            icon1 = QIcon.fromTheme(iconThemeName)
        else:
            icon1.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)
        
        self.browseButton.setIcon(icon1)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.browseButton)


        self.verticalLayout_2.addWidget(self.frame_7)

        self.frame_6 = QFrame(self.frame_3)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.label_2 = QLabel(self.frame_6)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 10, 261, 17))

        self.verticalLayout_2.addWidget(self.frame_6)

        self.comboBox = QComboBox(self.frame_3)
        self.comboBox.setObjectName(u"comboBox")

        self.verticalLayout_2.addWidget(self.comboBox)

        self.comboBox_2 = QComboBox(self.frame_3)
        self.comboBox_2.setObjectName(u"comboBox_2")

        self.verticalLayout_2.addWidget(self.comboBox_2)

        self.comboBox_4 = QComboBox(self.frame_3)
        self.comboBox_4.setObjectName(u"comboBox_4")

        self.verticalLayout_2.addWidget(self.comboBox_4)

        self.comboBox_5 = QComboBox(self.frame_3)
        self.comboBox_5.setObjectName(u"comboBox_5")

        self.verticalLayout_2.addWidget(self.comboBox_5)


        self.horizontalLayout_3.addWidget(self.frame_3)

        self.toolBox.addItem(self.page, u"Selection des Donn\u00e9es")
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.page_3.setGeometry(QRect(0, 0, 320, 559))
        self.horizontalLayout_4 = QHBoxLayout(self.page_3)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.frame_4 = QFrame(self.page_3)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.pushButton_2 = QPushButton(self.frame_4)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(10, 20, 241, 25))
        icon2 = QIcon()
        iconThemeName = u"view-refresh"
        if QIcon.hasThemeIcon(iconThemeName):
            icon2 = QIcon.fromTheme(iconThemeName)
        else:
            icon2.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)
        
        self.pushButton_2.setIcon(icon2)

        self.horizontalLayout_4.addWidget(self.frame_4)

        self.toolBox.addItem(self.page_3, u"Propri\u00e9t\u00e9s du Graphique")
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2.setGeometry(QRect(0, 0, 320, 559))
        self.horizontalLayout_5 = QHBoxLayout(self.page_2)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.frame_5 = QFrame(self.page_2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_5)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frame_9 = QFrame(self.frame_5)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_9)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_3 = QLabel(self.frame_9)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(16777215, 50))
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_3)

        self.label_4 = QLabel(self.frame_9)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_5.addWidget(self.label_4)


        self.verticalLayout_4.addWidget(self.frame_9)

        self.pushButton_3 = QPushButton(self.frame_5)
        self.pushButton_3.setObjectName(u"pushButton_3")
        icon3 = QIcon()
        iconThemeName = u"appointment-new"
        if QIcon.hasThemeIcon(iconThemeName):
            icon3 = QIcon.fromTheme(iconThemeName)
        else:
            icon3.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)
        
        self.pushButton_3.setIcon(icon3)

        self.verticalLayout_4.addWidget(self.pushButton_3)


        self.horizontalLayout_5.addWidget(self.frame_5)

        self.toolBox.addItem(self.page_2, u"Programme d'entretien")

        self.verticalLayout_3.addWidget(self.toolBox)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.horizontalLayout_2.addWidget(self.scrollArea)


        self.horizontalLayout.addWidget(self.frame)

        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout_2 = QGridLayout(self.tab_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.plotWidget_hist = QWidget(self.tab_2)
        self.plotWidget_hist.setObjectName(u"plotWidget_hist")

        self.gridLayout_2.addWidget(self.plotWidget_hist, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.gridLayout_3 = QGridLayout(self.tab_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.plotWidget_hist2 = QWidget(self.tab_3)
        self.plotWidget_hist2.setObjectName(u"plotWidget_hist2")

        self.gridLayout_3.addWidget(self.plotWidget_hist2, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_3, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout = QGridLayout(self.tab)
        self.gridLayout.setObjectName(u"gridLayout")
        self.plotWidget = QWidget(self.tab)
        self.plotWidget.setObjectName(u"plotWidget")

        self.gridLayout.addWidget(self.plotWidget, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab, "")

        self.horizontalLayout.addWidget(self.tabWidget)

        Main_Window.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(Main_Window)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1176, 22))
        Main_Window.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(Main_Window)
        self.statusbar.setObjectName(u"statusbar")
        Main_Window.setStatusBar(self.statusbar)

        self.retranslateUi(Main_Window)

        self.toolBox.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Main_Window)
    # setupUi

    def retranslateUi(self, Main_Window):
        Main_Window.setWindowTitle(QCoreApplication.translate("Main_Window", u"Predictive Maintenance", None))
        self.fileName.setText(QCoreApplication.translate("Main_Window", u"nom du fichier", None))
        self.browseButton.setText(QCoreApplication.translate("Main_Window", u"Rechercher", None))
        self.label_2.setText(QCoreApplication.translate("Main_Window", u"Information sur le fichier :", None))
        self.comboBox.setCurrentText("")
        self.comboBox.setPlaceholderText(QCoreApplication.translate("Main_Window", u"Flotte", None))
        self.comboBox_2.setPlaceholderText(QCoreApplication.translate("Main_Window", u"Equippement", None))
        self.comboBox_4.setCurrentText("")
        self.comboBox_4.setPlaceholderText(QCoreApplication.translate("Main_Window", u"Num\u00e9ro de la pi\u00e8ce", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), QCoreApplication.translate("Main_Window", u"Selection des Donn\u00e9es", None))
        self.pushButton_2.setText(QCoreApplication.translate("Main_Window", u"Actualiser", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_3), QCoreApplication.translate("Main_Window", u"Propri\u00e9t\u00e9s du Graphique", None))
        self.label_3.setText(QCoreApplication.translate("Main_Window", u"Programme d'entretien actuelle :", None))
        self.label_4.setText(QCoreApplication.translate("Main_Window", u"<html><head/><body><p>Num\u00e9ro de la t\u00e2che :</p><p>P/N : </p><p>Type de suivi :</p><p>P\u00e9riodicit\u00e9 :</p></body></html>", None))
        self.pushButton_3.setText(QCoreApplication.translate("Main_Window", u"Nouveau programme d'entretien", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), QCoreApplication.translate("Main_Window", u"Programme d'entretien", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("Main_Window", u"Total Occurency", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("Main_Window", u"Occurency Leading To Part Remplacement", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("Main_Window", u"Linear Regression", None))
    # retranslateUi

