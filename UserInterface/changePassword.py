from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class Ui_ChangePasswordWindow(object):
    
    def setupUi(self, ChangePasswordWindow):
        ChangePasswordWindow.setObjectName("ChangePasswordWindow")
        ChangePasswordWindow.resize(730, 730)
        icon = QtGui.QIcon()
        absolute_path=sys.path[0]
        icon.addPixmap(QtGui.QPixmap(absolute_path+"/images/app_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        ChangePasswordWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(ChangePasswordWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout_4.addWidget(self.label)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem2)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 4, 0, 1, 1)
        self.questionComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.questionComboBox.setObjectName("questionComboBox")
        self.questionComboBox.addItem("")
        self.questionComboBox.addItem("")
        self.questionComboBox.addItem("")
        self.questionComboBox.addItem("")
        self.questionComboBox.addItem("")
        self.gridLayout.addWidget(self.questionComboBox, 6, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.newPasswordLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.newPasswordLineEdit.setObjectName("newPasswordLineEdit")
        self.newPasswordLineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.gridLayout.addWidget(self.newPasswordLineEdit, 2, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 6, 0, 1, 1)
        self.confirmLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.confirmLineEdit.setObjectName("confirmLineEdit")
        self.confirmLineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.gridLayout.addWidget(self.confirmLineEdit, 4, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.answerLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.answerLineEdit.setObjectName("answerLineEdit")
        self.gridLayout.addWidget(self.answerLineEdit, 7, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem3, 5, 0, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem4, 3, 0, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem5, 1, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 3, 1, 1, 1)
        self.verticalLayout_4.addLayout(self.gridLayout)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem6)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem7)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.changePasswordButton = QtWidgets.QPushButton(self.centralwidget)
        self.changePasswordButton.setObjectName("changePasswordButton")
        self.verticalLayout_2.addWidget(self.changePasswordButton)
        self.cancelButton = QtWidgets.QPushButton(self.centralwidget)
        self.cancelButton.setObjectName("cancelButton")
        self.verticalLayout_2.addWidget(self.cancelButton)
        self.horizontalLayout_5.addLayout(self.verticalLayout_2)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem8)
        self.verticalLayout_4.addLayout(self.horizontalLayout_5)
        self.verticalLayout_5.addLayout(self.verticalLayout_4)
        ChangePasswordWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(ChangePasswordWindow)
        self.statusbar.setObjectName("statusbar")
        ChangePasswordWindow.setStatusBar(self.statusbar)

        self.retranslateUi(ChangePasswordWindow)
        QtCore.QMetaObject.connectSlotsByName(ChangePasswordWindow)

    def retranslateUi(self, ChangePasswordWindow):
        _translate = QtCore.QCoreApplication.translate
        ChangePasswordWindow.setWindowTitle(_translate("ChangePasswordWindow", "MainWindow"))
        self.label.setText(_translate("ChangePasswordWindow", "<html><head/><body><p><span style=\" font-size:26pt;\">Change Password</span></p></body></html>"))
        self.label_4.setText(_translate("ChangePasswordWindow", "<html><head/><body><p><span style=\" font-size:16pt;\">Confirm New Password :</span></p></body></html>"))
        self.questionComboBox.setItemText(0, _translate("ChangePasswordWindow", "What is the name of your pet?"))
        self.questionComboBox.setItemText(1, _translate("ChangePasswordWindow", "What is your mom\'s name?"))
        self.questionComboBox.setItemText(2, _translate("ChangePasswordWindow", "Where do you live?"))
        self.questionComboBox.setItemText(3, _translate("ChangePasswordWindow", "What school do you attend?"))
        self.questionComboBox.setItemText(4, _translate("ChangePasswordWindow", "What is your favorite food?"))
        self.label_3.setText(_translate("ChangePasswordWindow", "<html><head/><body><p><span style=\" font-size:16pt;\">New Password :</span></p></body></html>"))
        self.label_5.setText(_translate("ChangePasswordWindow", "<html><head/><body><p><span style=\" font-size:16pt;\">Confirm Security Question :</span></p></body></html>"))
        self.label_6.setText(_translate("ChangePasswordWindow", "<html><head/><body><p><span style=\" font-family:\'Whitney,Helvetica Neue,Helvetica,Arial,sans-serif\'; font-size:9pt; color:#ff6666; background-color:rgba(4,4,5,0.066667);\">*password must be between 6-20 characters and must contain a letter, a number </span></p><p><span style=\" font-family:\'Whitney,Helvetica Neue,Helvetica,Arial,sans-serif\'; font-size:9pt; color:#ff6666; background-color:rgba(4,4,5,0.066667);\">&nbsp;&nbsp;and a special character</span></p></body></html>"))
        self.changePasswordButton.setText(_translate("ChangePasswordWindow", "Change Password"))
        self.cancelButton.setText(_translate("ChangePasswordWindow", "Cancel"))
