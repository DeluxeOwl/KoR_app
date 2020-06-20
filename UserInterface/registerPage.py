from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_RegisterWindow(object):
    def setupUi(self, RegisterWindow):
        RegisterWindow.setObjectName("RegisterWindow")
        RegisterWindow.resize(730, 730)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./images/app_icon.png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        RegisterWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(RegisterWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 1, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 1, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 1, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_2)
        spacerItem2 = QtWidgets.QSpacerItem(
            0, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.comboBoxSecurityQuestion = QtWidgets.QComboBox(self.centralwidget)
        self.comboBoxSecurityQuestion.setObjectName("comboBoxSecurityQuestion")
        self.comboBoxSecurityQuestion.addItem("")
        self.comboBoxSecurityQuestion.addItem("")
        self.comboBoxSecurityQuestion.addItem("")
        self.comboBoxSecurityQuestion.addItem("")
        self.comboBoxSecurityQuestion.addItem("")
        self.gridLayout_3.addWidget(self.comboBoxSecurityQuestion, 8, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem3, 7, 0, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem4, 3, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 0, 0, 1, 1)
        self.passwordRegInput = QtWidgets.QLineEdit(self.centralwidget)
        self.passwordRegInput.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordRegInput.setObjectName("passwordRegInput")
        self.gridLayout_3.addWidget(self.passwordRegInput, 2, 1, 1, 1)
        self.usernameRegInput = QtWidgets.QLineEdit(self.centralwidget)
        self.usernameRegInput.setObjectName("usernameRegInput")
        self.gridLayout_3.addWidget(self.usernameRegInput, 0, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout_3.addWidget(self.label_4, 4, 0, 1, 1)
        self.confirmRegPasswordInput = QtWidgets.QLineEdit(self.centralwidget)
        self.confirmRegPasswordInput.setEchoMode(QtWidgets.QLineEdit.Password)
        self.confirmRegPasswordInput.setObjectName("confirmRegPasswordInput")
        self.gridLayout_3.addWidget(self.confirmRegPasswordInput, 4, 1, 1, 1)
        self.roleRegSelect = QtWidgets.QComboBox(self.centralwidget)
        self.roleRegSelect.setObjectName("roleRegSelect")
        self.roleRegSelect.addItem("")
        self.roleRegSelect.addItem("")
        self.gridLayout_3.addWidget(self.roleRegSelect, 6, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout_3.addWidget(self.label_3, 2, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout_3.addWidget(self.label_5, 6, 0, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem5, 5, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout_3.addWidget(self.label_6, 1, 1, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem6, 1, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setObjectName("label_7")
        self.gridLayout_3.addWidget(self.label_7, 3, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setObjectName("label_8")
        self.gridLayout_3.addWidget(self.label_8, 8, 0, 1, 1)
        self.lineEditSecurityAnswer = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditSecurityAnswer.setObjectName("lineEditSecurityAnswer")
        self.gridLayout_3.addWidget(self.lineEditSecurityAnswer, 9, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_3)
        spacerItem7 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem7)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem8 = QtWidgets.QSpacerItem(
            30, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem8)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.signUpRegButton = QtWidgets.QPushButton(self.centralwidget)
        self.signUpRegButton.setObjectName("signUpRegButton")
        self.verticalLayout_2.addWidget(self.signUpRegButton)
        self.cancelRegButton = QtWidgets.QPushButton(self.centralwidget)
        self.cancelRegButton.setObjectName("cancelRegButton")
        self.verticalLayout_2.addWidget(self.cancelRegButton)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        spacerItem9 = QtWidgets.QSpacerItem(
            30, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem9)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        RegisterWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(RegisterWindow)
        self.statusbar.setObjectName("statusbar")
        RegisterWindow.setStatusBar(self.statusbar)

        self.retranslateUi(RegisterWindow)
        QtCore.QMetaObject.connectSlotsByName(RegisterWindow)

    def retranslateUi(self, RegisterWindow):
        _translate = QtCore.QCoreApplication.translate
        RegisterWindow.setWindowTitle(
            _translate("RegisterWindow", "Register Page"))
        self.label.setText(_translate(
            "RegisterWindow", "<html><head/><body><p><span style=\" font-size:26pt;\">Register</span></p></body></html>"))
        self.comboBoxSecurityQuestion.setItemText(0, _translate(
            "RegisterWindow", "What is the name of your pet?"))
        self.comboBoxSecurityQuestion.setItemText(
            1, _translate("RegisterWindow", "What is your mom\'s name?"))
        self.comboBoxSecurityQuestion.setItemText(
            2, _translate("RegisterWindow", "Where do you live?"))
        self.comboBoxSecurityQuestion.setItemText(
            3, _translate("RegisterWindow", "What school do you attend?"))
        self.comboBoxSecurityQuestion.setItemText(4, _translate(
            "RegisterWindow", "What is your favorite food?"))
        self.label_2.setText(_translate(
            "RegisterWindow", "<html><head/><body><p><span style=\" font-size:16pt;\">Username :</span></p></body></html>"))
        self.label_4.setText(_translate(
            "RegisterWindow", "<html><head/><body><p><span style=\" font-size:16pt;\">Confirm Password :</span></p></body></html>"))
        self.roleRegSelect.setItemText(0, _translate("RegisterWindow", "User"))
        self.roleRegSelect.setItemText(
            1, _translate("RegisterWindow", "Guest"))
        self.label_3.setText(_translate(
            "RegisterWindow", "<html><head/><body><p><span style=\" font-size:16pt;\">Password :</span></p></body></html>"))
        self.label_5.setText(_translate(
            "RegisterWindow", "<html><head/><body><p><span style=\" font-size:16pt;\">Role :</span></p></body></html>"))
        self.label_6.setText(_translate("RegisterWindow", "<html><head/><body><p><span style=\" font-family:\'Whitney,Helvetica Neue,Helvetica,Arial,sans-serif\'; font-size:9pt; color:#ff6666; background-color:rgba(4,4,5,0.066667);\">*username must be between 6-20 characters and must contain letters, numbers </span></p><p><span style=\" font-family:\'Whitney,Helvetica Neue,Helvetica,Arial,sans-serif\'; font-size:9pt; color:#ff6666; background-color:rgba(4,4,5,0.066667);\">&nbsp;&nbsp;and underscores</span></p></body></html>"))
        self.label_7.setText(_translate("RegisterWindow", "<html><head/><body><p><span style=\" font-family:\'Whitney,Helvetica Neue,Helvetica,Arial,sans-serif\'; font-size:9pt; color:#ff6666; background-color:rgba(4,4,5,0.066667);\">*password must be between 6-20 characters and must contain a letter, a number </span></p><p><span style=\" font-family:\'Whitney,Helvetica Neue,Helvetica,Arial,sans-serif\'; font-size:9pt; color:#ff6666; background-color:rgba(4,4,5,0.066667);\">&nbsp;&nbsp;and a special character</span></p></body></html>"))
        self.label_8.setText(_translate(
            "RegisterWindow", "<html><head/><body><p><span style=\" font-size:16pt;\">Security question :</span></p></body></html>"))
        self.signUpRegButton.setText(_translate("RegisterWindow", "Sign Up"))
        self.cancelRegButton.setText(_translate("RegisterWindow", "Cancel"))
