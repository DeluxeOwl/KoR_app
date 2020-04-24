#!/usr/bin/python3
from PyQt5 import QtWidgets

from UserInterface.mainPage import Ui_MainWindow
from UserInterface.registerPage import Ui_RegisterWindow
from BackEndActions.ButtonActions import *

import sys
import os
import sqlite3


def switchToWindow(windowToSwitchTo):

    # Get old window sizes
    newWidth = MainWindow.frameSize().width()
    newHeight = MainWindow.frameSize().height()

    # Make the window appear
    ui = windowToSwitchTo()
    ui.setupUi(MainWindow)
    MainWindow.show()

    # Adjust the size in case the user stretched the window
    MainWindow.resize(newWidth, newHeight)

    # Ui_RegisterWindow buttons
    if type(ui) is Ui_RegisterWindow:
        ui.cancelRegButton.clicked.connect(
            lambda: switchToWindow(Ui_MainWindow))
        ui.signUpRegButton.clicked.connect(
            lambda: registerButtonClicked(ui, conn, cursor))

    # Ui_MainWindow buttons
    if type(ui) is Ui_MainWindow:
        ui.loginButton.clicked.connect(
            lambda: loginButtonClicked(ui, conn, cursor))

        ui.registerButton.clicked.connect(
            lambda: switchToWindow(Ui_RegisterWindow))

        ui.forgotpasswordButton.clicked.connect(
            lambda: forgotpasswordButtonClicked(ui, conn, cursor))


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
                ''' CREATE TABLE user_info (username text,
                                            password text,
                                            role text,
                                            UNIQUE(username))''')
            conn.commit()

        # Default admin account
        cursor.execute(
            ''' SELECT COUNT(*) FROM user_info WHERE username='admin' ''')
        if cursor.fetchone()[0] == 0:
            cursor.execute(
                "INSERT INTO user_info VALUES (?,?,?)", ('admin', EncryptLibrary.hashPassword('admin'), 'Admin'))
            conn.commit()

        """--------------------"""

        app = QtWidgets.QApplication(sys.argv)

        """ This needs to be in main only for the first page """
        MainWindow = QtWidgets.QMainWindow()

        ui = Ui_MainWindow()
        ui.setupUi(MainWindow)

        ui.loginButton.clicked.connect(
            lambda: loginButtonClicked(ui, conn, cursor))

        ui.registerButton.clicked.connect(
            lambda: switchToWindow(Ui_RegisterWindow))

        ui.forgotpasswordButton.clicked.connect(
            lambda: forgotpasswordButtonClicked(ui, conn, cursor))

        """Add more MainWindow related buttons above and in switchToWindow"""

        MainWindow.show()

        sys.exit(app.exec_())
    finally:
        print("This is executed as the app exits")
        conn.close()
