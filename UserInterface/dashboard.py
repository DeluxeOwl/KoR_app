# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dashboard.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_LoggedWindow(object):
    def setupUi(self, LoggedWindow):
        LoggedWindow.setObjectName("LoggedWindow")
        LoggedWindow.resize(730, 730)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./images/app_icon.png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        LoggedWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(LoggedWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 1, 1, 1)
        self.treeView = QtWidgets.QTreeView(self.centralwidget)
        self.treeView.setObjectName("treeView")
        self.gridLayout.addWidget(self.treeView, 1, 0, 1, 5)
        self.pushButtonLogout = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonLogout.setObjectName("pushButtonLogout")
        self.gridLayout.addWidget(self.pushButtonLogout, 0, 4, 1, 1)
        self.labelUsername = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.labelUsername.setFont(font)
        self.labelUsername.setObjectName("labelUsername")
        self.gridLayout.addWidget(self.labelUsername, 0, 0, 1, 1)
        self.pushButtonChangePassword = QtWidgets.QPushButton(
            self.centralwidget)
        self.pushButtonChangePassword.setObjectName("pushButtonChangePassword")
        self.gridLayout.addWidget(self.pushButtonChangePassword, 0, 3, 1, 1)
        self.pushButtonGroups = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonGroups.setObjectName("pushButtonGroups")
        self.gridLayout.addWidget(self.pushButtonGroups, 0, 2, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        LoggedWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(LoggedWindow)
        QtCore.QMetaObject.connectSlotsByName(LoggedWindow)

    def retranslateUi(self, LoggedWindow):
        _translate = QtCore.QCoreApplication.translate
        LoggedWindow.setWindowTitle(_translate("LoggedWindow", "Dashboard"))
        self.pushButtonLogout.setText(_translate("LoggedWindow", "Log out"))
        self.labelUsername.setText(_translate("LoggedWindow", "Username"))
        self.pushButtonChangePassword.setText(
            _translate("LoggedWindow", "Change Password"))
        self.pushButtonGroups.setText(_translate("LoggedWindow", "Groups"))
