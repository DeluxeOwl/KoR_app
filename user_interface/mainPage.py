# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainPage.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(731, 726)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../images/app_icon.png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.verticalSpacer = QtWidgets.QLabel(self.centralwidget)
        self.verticalSpacer.setText("")
        self.verticalSpacer.setPixmap(QtGui.QPixmap(
            "../../.designer/backup/images/main_image.png"))
        self.verticalSpacer.setObjectName("verticalSpacer")
        self.gridLayout_3.addWidget(self.verticalSpacer, 0, 1, 1, 1)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.usernameInput = QtWidgets.QLineEdit(self.centralwidget)
        self.usernameInput.setObjectName("usernameInput")
        self.formLayout.setWidget(
            1, QtWidgets.QFormLayout.FieldRole, self.usernameInput)
        self.passwordInput = QtWidgets.QLineEdit(self.centralwidget)
        self.passwordInput.setInputMethodHints(
            QtCore.Qt.ImhHiddenText | QtCore.Qt.ImhNoAutoUppercase | QtCore.Qt.ImhNoPredictiveText | QtCore.Qt.ImhSensitiveData)
        self.passwordInput.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordInput.setObjectName("passwordInput")
        self.formLayout.setWidget(
            3, QtWidgets.QFormLayout.FieldRole, self.passwordInput)
        spacerItem = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.formLayout.setItem(4, QtWidgets.QFormLayout.FieldRole, spacerItem)
        spacerItem1 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.formLayout.setItem(
            0, QtWidgets.QFormLayout.FieldRole, spacerItem1)
        self.usernameText = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.usernameText.sizePolicy().hasHeightForWidth())
        self.usernameText.setSizePolicy(sizePolicy)
        self.usernameText.setObjectName("usernameText")
        self.formLayout.setWidget(
            1, QtWidgets.QFormLayout.LabelRole, self.usernameText)
        self.passwordText = QtWidgets.QLabel(self.centralwidget)
        self.passwordText.setObjectName("passwordText")
        self.formLayout.setWidget(
            3, QtWidgets.QFormLayout.LabelRole, self.passwordText)
        self.gridLayout_3.addLayout(self.formLayout, 0, 2, 1, 1)
        self.mainImage = QtWidgets.QLabel(self.centralwidget)
        self.mainImage.setText("")
        self.mainImage.setPixmap(QtGui.QPixmap("../images/main_image.png"))
        self.mainImage.setObjectName("mainImage")
        self.gridLayout_3.addWidget(self.mainImage, 0, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout_3, 0, 0, 1, 1)
        self.forgotpasswordButton = QtWidgets.QPushButton(self.centralwidget)
        self.forgotpasswordButton.setObjectName("forgotpasswordButton")
        self.gridLayout_2.addWidget(self.forgotpasswordButton, 6, 0, 1, 1)
        self.register_button = QtWidgets.QPushButton(self.centralwidget)
        self.register_button.setObjectName("register_button")
        self.gridLayout_2.addWidget(self.register_button, 3, 0, 1, 1)
        self.loginButton = QtWidgets.QPushButton(self.centralwidget)
        self.loginButton.setObjectName("loginButton")
        self.gridLayout_2.addWidget(self.loginButton, 1, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 3, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate(
            "MainWindow", "KoR - Safe vault APP"))
        self.usernameText.setText(_translate("MainWindow", "Username"))
        self.passwordText.setText(_translate("MainWindow", "Password"))
        self.forgotpasswordButton.setText(
            _translate("MainWindow", "Forgot password"))
        self.register_button.setText(_translate("MainWindow", "Register"))
        self.loginButton.setText(_translate("MainWindow", "Login"))
