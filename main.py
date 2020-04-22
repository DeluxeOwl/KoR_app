#!/usr/bin/python3
from PyQt5 import QtWidgets
# importing our generated file
from user_interface.mainPage import Ui_MainWindow

import sys
sys.path.append('~/KorApp/')


class mywindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


app = QtWidgets.QApplication([])
application = mywindow()
application.show()
sys.exit(app.exec())
