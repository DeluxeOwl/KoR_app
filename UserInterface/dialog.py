from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 250)
        Dialog.setMaximumSize(QtCore.QSize(500, 300))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./images/app_icon.png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 3, 1, 1)
        self.lineEditAnswer = QtWidgets.QLineEdit(Dialog)
        self.lineEditAnswer.setObjectName("lineEditAnswer")
        self.gridLayout.addWidget(self.lineEditAnswer, 2, 1, 1, 2)
        self.pushButtonOK = QtWidgets.QPushButton(Dialog)
        self.pushButtonOK.setObjectName("pushButtonOK")
        self.gridLayout.addWidget(self.pushButtonOK, 3, 1, 1, 2)
        self.labelQuestion = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.labelQuestion.setFont(font)
        self.labelQuestion.setObjectName("labelQuestion")
        self.gridLayout.addWidget(self.labelQuestion, 1, 2, 1, 1)
        self.pushButtonCancel = QtWidgets.QPushButton(Dialog)
        self.pushButtonCancel.setObjectName("pushButtonCancel")
        self.gridLayout.addWidget(self.pushButtonCancel, 4, 1, 1, 2)
        spacerItem1 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 3, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButtonOK.setText(_translate("Dialog", "OK"))
        self.labelQuestion.setText(_translate("Dialog", "Are you sure?"))
        self.pushButtonCancel.setText(_translate("Dialog", "Cancel"))

    def changeText(self, text):
        _translate = QtCore.QCoreApplication.translate
        self.labelQuestion.setText(_translate("Dialog", str(text)))

    def getLineEditAnswer(self):
        return self.lineEditAnswer.text()
