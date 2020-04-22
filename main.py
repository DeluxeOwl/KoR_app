#!/usr/bin/python3
from PyQt5 import QtWidgets
# importing our generated file
from UserInterface.mainPage import Ui_MainWindow
from BackEndActions.ButtonActions import *

import sys


class MyWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(MyWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # Use lambda to be able to use arguments
        self.ui.loginButton.clicked.connect(
            lambda: loginButtonClicked("something"))


try:
    app = QtWidgets.QApplication([])
    application = MyWindow()
    application.show()
    sys.exit(app.exec())
finally:
    print("This is executed as the app exits")
