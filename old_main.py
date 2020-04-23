#!/usr/bin/python3
from PyQt5 import QtWidgets
# importing our generated file
from UserInterface.mainPage import Ui_MainWindow
from BackEndActions.ButtonActions import *

import sys
import os
import sqlite3


class MyWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(MyWindow, self).__init__()
        self.initializeVariables()
        self.databaseConnection()
        self.buttonClickActions()

    def initializeVariables(self):
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.database = os.path.dirname(
            os.path.abspath(__file__))+'/BackEndActions/users.db'

    def databaseConnection(self):
        self.conn = sqlite3.connect(self.database)
        self.c = self.conn.cursor()

        # Check if table exists,if not,create it
        self.c.execute(
            ''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='user_info' ''')
        if self.c.fetchone()[0] == 0:
            self.c.execute(
                ''' CREATE TABLE user_info (username text,password text,UNIQUE(username))''')
            self.conn.commit()

    def buttonClickActions(self):
        # Use lambda to be able to use arguments
        self.ui.loginButton.clicked.connect(
            lambda: loginButtonClicked("something"))
        self.ui.registerButton.clicked.connect(
            lambda: registerButtonClicked('John', 'strongpassw@@@@@rd', self.conn, self.c))
        self.ui.forgotpasswordButton.clicked.connect(
            lambda: forgotpasswordButtonClicked('I forgot it again'))


try:
    app = QtWidgets.QApplication([])
    application = MyWindow()
    application.show()
    sys.exit(app.exec())
finally:
    print("This is executed as the app exits")
