# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dashboard.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import subprocess


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
        self.pushButtonChangePassword = QtWidgets.QPushButton(
            self.centralwidget)
        self.pushButtonChangePassword.setObjectName("pushButtonChangePassword")
        self.gridLayout.addWidget(self.pushButtonChangePassword, 0, 4, 1, 1)
        self.pushButtonLogout = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonLogout.setObjectName("pushButtonLogout")
        self.gridLayout.addWidget(self.pushButtonLogout, 0, 5, 1, 1)

        self.treeView = QtWidgets.QTreeView(self.centralwidget)
        self.treeView.setObjectName("treeView")

        self.gridLayout.addWidget(self.treeView, 1, 0, 1, 6)
        self.pushButtonGroups = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonGroups.setObjectName("pushButtonGroups")
        self.gridLayout.addWidget(self.pushButtonGroups, 0, 3, 1, 1)
        self.labelUsername = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.labelUsername.setFont(font)
        self.labelUsername.setObjectName("labelUsername")
        self.gridLayout.addWidget(self.labelUsername, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 1, 1, 1)
        self.pushButtonOpenFiles = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonOpenFiles.setObjectName("pushButtonOpenFiles")
        self.gridLayout.addWidget(self.pushButtonOpenFiles, 0, 2, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        LoggedWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(LoggedWindow)
        QtCore.QMetaObject.connectSlotsByName(LoggedWindow)

        self.setDirectory()

        # For the context menu on right click
        self.treeView.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.treeView.customContextMenuRequested.connect(self.context_menu)

    def retranslateUi(self, LoggedWindow):
        _translate = QtCore.QCoreApplication.translate
        LoggedWindow.setWindowTitle(_translate("LoggedWindow", "Dashboard"))
        self.pushButtonChangePassword.setText(
            _translate("LoggedWindow", "Change Password"))
        self.pushButtonLogout.setText(_translate("LoggedWindow", "Log out"))
        self.pushButtonGroups.setText(_translate("LoggedWindow", "Groups"))
        self.labelUsername.setText(_translate("LoggedWindow", "Username"))
        self.pushButtonOpenFiles.setText(
            _translate("LoggedWindow", "Open Files"))

    def setDirectory(self, dir=''):
        # Handle filesystem
        self.model = QtWidgets.QFileSystemModel()
        self.model.setRootPath(QtCore.QDir.rootPath()
                               )              # Get root path
        self.treeView.setModel(self.model)
        self.treeView.setRootIndex(self.model.index(
            "/home"+dir))  # Choose directory to display

    # For the context menu on right click

    def context_menu(self):
        menu = QtWidgets.QMenu()
        openButton = menu.addAction("Open")
        openButton.triggered.connect(self.open_file)

        cursor = QtGui.QCursor()
        menu.exec_(cursor.pos())

    def open_file(self):
        index = self.treeView.currentIndex()
        file_path = self.model.filePath(index)
        print(file_path)

        # open for windows,xdg-open for linux
        subprocess.run(['xdg-open', file_path], check=True)
