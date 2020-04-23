#!/usr/bin/python3
from PyQt5 import QtWidgets

from UserInterface.mainPage import Ui_MainWindow
from UserInterface.registerPage import Ui_RegisterWindow
from BackEndActions.ButtonActions import *

import sys
import os
import sqlite3


def switchToWindow(windowToSwitchTo):
    # Make the window appear
    ui = windowToSwitchTo()
    ui.setupUi(MainWindow)
    MainWindow.show()

    # Ui_RegisterWindow buttons
    if type(ui) is Ui_RegisterWindow:
        ui.cancelRegButton.clicked.connect(
            lambda: switchToWindow(Ui_MainWindow))
        # TODO: take data from labels
        ui.signUpRegButton.clicked.connect(
            lambda: registerButtonClicked('John', '1234', conn, cursor))

    # Ui_MainWindow buttons
    if type(ui) is Ui_MainWindow:
        ui.loginButton.clicked.connect(
            lambda: loginButtonClicked("something"))

        ui.registerButton.clicked.connect(
            lambda: switchToWindow(Ui_RegisterWindow))


if __name__ == "__main__":
    try:
        """start database"""
        database_path = os.path.dirname(
            os.path.abspath(__file__))+'/BackEndActions/users.db'
        conn = sqlite3.connect(database_path)
        cursor = conn.cursor()
        # Check if table exists,if not,create it
        cursor.execute(
            ''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='user_info' ''')
        if cursor.fetchone()[0] == 0:
            cursor.execute(
                ''' CREATE TABLE user_info (username text,password text,UNIQUE(username))''')
            conn.commit()
        """--------------------"""

        app = QtWidgets.QApplication(sys.argv)

        """ This needs to be in main only for the first page """
        MainWindow = QtWidgets.QMainWindow()

        ui = Ui_MainWindow()
        ui.setupUi(MainWindow)

        ui.loginButton.clicked.connect(
            lambda: loginButtonClicked("something"))

        ui.registerButton.clicked.connect(
            lambda: switchToWindow(Ui_RegisterWindow))

        """Add more MainWindow related buttons above and in switchToWindow"""

        MainWindow.show()

        sys.exit(app.exec_())
    finally:
        print("This is executed as the app exits")
        conn.close()
