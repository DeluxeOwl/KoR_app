#!/usr/bin/python3
from PyQt5 import QtWidgets, uic

import sys

app = QtWidgets.QApplication([])

# specify the location of your .ui file
win = uic.loadUi("../user_interface/mainPage.ui")

win.show()

sys.exit(app.exec())
