from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class Ui_GroupWindow(object):

    def __init__(self):
        # The main connection to the users database
        self.usersConn = None
        self.usersCursor = None

    def setupUi(self, GroupWindow):
        GroupWindow.setObjectName("GroupWindow")
        GroupWindow.resize(730, 730)

        icon = QtGui.QIcon()
        absolute_path=sys.path[0]
        icon.addPixmap(QtGui.QPixmap(absolute_path+"/images/app_icon.png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        GroupWindow.setWindowIcon(icon)

        self.centralwidget = QtWidgets.QWidget(GroupWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.disbandGroupButton = QtWidgets.QPushButton(self.centralwidget)
        self.disbandGroupButton.setObjectName("disbandGroupButton")
        self.gridLayout.addWidget(self.disbandGroupButton, 4, 1, 1, 2)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 1, 1, 2)
        self.leaveGroupButton = QtWidgets.QPushButton(self.centralwidget)
        self.leaveGroupButton.setObjectName("leaveGroupButton")
        self.gridLayout.addWidget(self.leaveGroupButton, 3, 1, 1, 2)

        self.groupTree = QtWidgets.QTreeWidget(self.centralwidget)
        self.groupTree.setObjectName("groupTree")
        self.groupTree.headerItem().setText(0, "Groups")
        self.gridLayout.addWidget(self.groupTree, 0, 0, 15, 1)

        self.groupComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.groupComboBox.setObjectName("groupComboBox")
        self.gridLayout.addWidget(self.groupComboBox, 1, 1, 1, 2)
        self.newGroupButton = QtWidgets.QPushButton(self.centralwidget)
        self.newGroupButton.setObjectName("newGroupButton")
        self.gridLayout.addWidget(self.newGroupButton, 2, 1, 1, 1)
        self.openFilesButton = QtWidgets.QPushButton(self.centralwidget)
        self.openFilesButton.setObjectName("openFilesButton")
        self.gridLayout.addWidget(self.openFilesButton, 2, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 5, 1, 1, 2)
        self.userComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.userComboBox.setObjectName("userComboBox")
        self.gridLayout.addWidget(self.userComboBox, 6, 1, 1, 2)
        self.addToGroupButton = QtWidgets.QPushButton(self.centralwidget)
        self.addToGroupButton.setObjectName("addToGroupButton")
        self.gridLayout.addWidget(self.addToGroupButton, 7, 1, 1, 2)
        self.removeFromGroupButton = QtWidgets.QPushButton(self.centralwidget)
        self.removeFromGroupButton.setObjectName("removeFromGroupButton")
        self.gridLayout.addWidget(self.removeFromGroupButton, 8, 1, 1, 2)
        self.appointLeaderButton = QtWidgets.QPushButton(self.centralwidget)
        self.appointLeaderButton.setObjectName("appointLeaderButton")
        self.gridLayout.addWidget(self.appointLeaderButton, 9, 1, 1, 2)
        self.deleteUserButton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        self.deleteUserButton.setFont(font)
        self.deleteUserButton.setObjectName("deleteUserButton")
        self.gridLayout.addWidget(self.deleteUserButton, 10, 1, 1, 2)
        self.takeMeBackButton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.takeMeBackButton.setFont(font)
        self.takeMeBackButton.setIconSize(QtCore.QSize(16, 16))
        self.takeMeBackButton.setCheckable(False)
        self.takeMeBackButton.setChecked(False)
        self.takeMeBackButton.setObjectName("takeMeBackButton")
        self.gridLayout.addWidget(self.takeMeBackButton, 12, 1, 3, 2)
        GroupWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(GroupWindow)
        QtCore.QMetaObject.connectSlotsByName(GroupWindow)

    def retranslateUi(self, GroupWindow):
        _translate = QtCore.QCoreApplication.translate
        GroupWindow.setWindowTitle(_translate("GroupWindow", "Groups"))
        self.disbandGroupButton.setText(
            _translate("GroupWindow", "Disband group"))
        self.label.setText(_translate("GroupWindow", "Select group:"))
        self.leaveGroupButton.setText(_translate("GroupWindow", "Leave group"))
        self.newGroupButton.setText(_translate("GroupWindow", "New group"))
        self.openFilesButton.setText(_translate("GroupWindow", "Open files"))
        self.label_2.setText(_translate("GroupWindow", "Select user:"))
        self.addToGroupButton.setText(
            _translate("GroupWindow", "Add to group"))
        self.removeFromGroupButton.setText(
            _translate("GroupWindow", "Remove from group"))
        self.appointLeaderButton.setText(
            _translate("GroupWindow", "Appoint leader"))
        self.deleteUserButton.setText(_translate("GroupWindow", "Delete user"))
        self.takeMeBackButton.setText(
            _translate("GroupWindow", "Take me back"))

    def displayGroupUsers(self, conn=None, c=None, currentUser=None):
        ''' Displays the groups and users in this window'''
        self.groupTree.clear()
        self.groupComboBox.clear()
        self.userComboBox.clear()

        c.execute("SELECT groupName,members,groupLeader from group_info")
        rows = c.fetchall()

        self.usersCursor.execute("SELECT username from user_info")
        rowsUser = self.usersCursor.fetchall()

        uniqueMembers = []
        for row in rowsUser:
            member = row[0]
            uniqueMembers.append(member)

        uniqueMembers = set(uniqueMembers)
        for member in uniqueMembers:
            self.userComboBox.addItem(member)

        for row in rows:
            groupName = row[0]
            members = row[1]
            groupLeader = row[2]

            self.groupComboBox.addItem(groupName)

            tmpGroup = QtWidgets.QTreeWidgetItem([groupName])
            self.groupTree.addTopLevelItem(tmpGroup)

            for member in members.split():
                if member == groupLeader:
                    tmpChild = QtWidgets.QTreeWidgetItem(["*"+member])
                    tmpGroup.addChild(tmpChild)
                else:
                    tmpChild = QtWidgets.QTreeWidgetItem([member])
                    tmpGroup.addChild(tmpChild)

        self.groupTree.expandToDepth(0)
