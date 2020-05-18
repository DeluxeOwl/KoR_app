# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dashboard.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from UserInterface.dialog import Ui_Dialog
import subprocess
import os


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
            os.environ['HOME']+dir))  # Choose directory to display

    # For the context menu on right click

    def context_menu(self):
        menu = QtWidgets.QMenu()
        openButton = menu.addAction("Open")
        openButton.triggered.connect(self.open_file)

        renameButton = menu.addAction("Rename")
        renameButton.triggered.connect(self.rename_file)

        deleteButton = menu.addAction("Delete")
        deleteButton.triggered.connect(self.delete_file)

        newfileButton = menu.addAction("New file")
        newfileButton.triggered.connect(self.new_file)

        cursor = QtGui.QCursor()
        menu.exec_(cursor.pos())

    def open_file(self):
        index = self.treeView.currentIndex()
        file_path = self.model.filePath(index)
        print("Opening", file_path)

        # open for windows,xdg-open for linux
        subprocess.run(['xdg-open', file_path], check=True)

    def rename_file(self):
        index = self.treeView.currentIndex()
        file_path = self.model.filePath(index)

        dialog = QtWidgets.QDialog()
        dialog.ui = Ui_Dialog()
        dialog.ui.setupUi(dialog)
        dialog.setAttribute(QtCore.Qt.WA_DeleteOnClose)

        dialog.ui.changeText("New name:")
        dialog.ui.pushButtonCancel.clicked.connect(dialog.done)

        def rename():
            # Get the length of the name of the file
            filenameLength = len(self.model.fileName(index))
            # Remove it so we only have the path
            onlyPath = file_path[0:len(file_path)-filenameLength]
            # Get the new name
            newName = dialog.ui.getLineEditAnswer()
            if newName.isspace():
                dialog.ui.changeText("Name cannot be blank.")
            else:
                try:
                    os.rename(file_path, onlyPath+newName)
                    print(file_path, "changed to", onlyPath+newName)
                    dialog.done(0)
                except NotADirectoryError:
                    dialog.ui.changeText("Name cannot be blank.")

        dialog.ui.pushButtonOK.clicked.connect(rename)

        dialog.exec_()

    def delete_file(self):
        index = self.treeView.currentIndex()
        file_path = self.model.filePath(index)

        dialog = QtWidgets.QDialog()
        dialog.ui = Ui_Dialog()
        dialog.ui.setupUi(dialog)
        dialog.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        dialog.ui.changeText("Are you sure? y/n")

        dialog.ui.pushButtonCancel.clicked.connect(dialog.done)

        def delete():
            answer = dialog.ui.getLineEditAnswer()
            if answer == "y":
                try:
                    if os.path.isdir(file_path):
                        os.rmdir(file_path)
                    else:
                        os.remove(file_path)
                    dialog.done(0)
                except OSError:
                    dialog.ui.changeText(
                        "Are you sure? y/n\nError:Directory not empty")
            elif answer == "n":
                dialog.done(0)
            else:
                dialog.ui.changeText(
                    "Are you sure? y/n\nInvalid answer")

        dialog.ui.pushButtonOK.clicked.connect(delete)

        dialog.exec_()

    def new_file(self):
        index = self.treeView.currentIndex()
        file_path = self.model.filePath(index)

        dialog = QtWidgets.QDialog()
        dialog.ui = Ui_Dialog()
        dialog.ui.setupUi(dialog)
        dialog.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        dialog.ui.changeText("Enter filename:")

        dialog.ui.pushButtonCancel.clicked.connect(dialog.done)

        def newfile():
            filename = dialog.ui.getLineEditAnswer()

            if os.path.isdir(file_path):
                subprocess.run(['touch', file_path+"/"+filename], check=True)
                dialog.done(0)
            elif os.path.isfile(file_path):
                # Get the length of the name of the file
                filenameLength = len(self.model.fileName(index))
                # Remove it so we only have the path
                onlyPath = file_path[0:len(file_path)-filenameLength]
                subprocess.run(['touch', onlyPath+"/"+filename], check=True)
                dialog.done(0)

        dialog.ui.pushButtonOK.clicked.connect(newfile)

        dialog.exec_()
