#!/usr/bin/python3
from PyQt5 import QtWidgets
# importing our generated file
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
    # Ui_MainWindow buttons
    if type(ui) is Ui_MainWindow:
        ui.loginButton.clicked.connect(
            lambda: loginButtonClicked("something"))

        ui.registerButton.clicked.connect(
            lambda: switchToWindow(Ui_RegisterWindow))


if __name__ == "__main__":
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
