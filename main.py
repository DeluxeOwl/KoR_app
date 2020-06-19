#!/usr/bin/python3
from PyQt5 import QtWidgets

from UserInterface.mainPage import Ui_MainWindow
from UserInterface.registerPage import Ui_RegisterWindow
from UserInterface.dashboard import Ui_LoggedWindow
from UserInterface.forgotPasswordPage import Ui_ForgotPasswordWindow
from UserInterface.changePassword import Ui_ChangePasswordWindow
from UserInterface.groupPage import Ui_GroupWindow
from BackEndActions.ButtonActions import *
from BackEndActions.EncryptLibrary import encryptFiles

import sys
import os
import sqlite3

# lastWindow is for checking if the last window was a groups window 
# and if it was,we display the files in UI_LoggedWindow
def switchToWindow(windowToSwitchTo, currentUser=None,lastWindow=None):

    # Get old window sizes
    newWidth = MainWindow.frameSize().width() - 8
    newHeight = MainWindow.frameSize().height() - 33

    # Make the window appear
    ui = windowToSwitchTo()
    ui.setupUi(MainWindow)
    MainWindow.show()

    # Adjust the size in case the user stretched the window
    MainWindow.resize(newWidth, newHeight)

    # Ui_RegisterWindow buttons
    if type(ui) is Ui_RegisterWindow:
        ui.cancelRegButton.clicked.connect(
            lambda: switchToWindow(Ui_MainWindow))
        ui.signUpRegButton.clicked.connect(
            lambda: registerButtonClicked(ui, switchToWindow, dataLocation, conn, cursor))

    # Ui_LoggedWindow buttons
    if type(ui) is Ui_LoggedWindow:
        ui.labelUsername.setText(currentUser)

        # We set the user's directory
        # TODO : change encrypt password for everyone
        if currentUser == "admin":
            ui.setDirectory(dataLocation)
            if lastWindow is None:
                encryptFiles(dataLocation, decrypt=True)
        else:
            # In case the admin deleted the directory
            if not os.path.isdir(dataLocation+"/"+currentUser):
                os.mkdir(dataLocation+"/"+currentUser)
            ui.setDirectory(dataLocation+"/"+currentUser)
            if lastWindow is None:
                encryptFiles(dataLocation+"/"+currentUser, decrypt=True)

        ui.pushButtonLogout.clicked.connect(
            lambda: logoutButtonClicked(switchToWindow, currentUser, conn, cursor))
        ui.pushButtonOpenFiles.clicked.connect(
            lambda: pushButtonOpenFilesClicked(ui, currentUser, conn, cursor)
        )
        ui.pushButtonChangePassword.clicked.connect(
            lambda:switchToWindow(Ui_ChangePasswordWindow,currentUser)
        )
        ui.pushButtonGroups.clicked.connect(
            lambda:switchToWindow(Ui_GroupWindow,currentUser)
        )

    # Ui_MainWindow buttons
    if type(ui) is Ui_MainWindow:
        ui.loginButton.clicked.connect(
            lambda: loginButtonClicked(ui, switchToWindow, conn, cursor))

        ui.registerButton.clicked.connect(
            lambda: switchToWindow(Ui_RegisterWindow))

        ui.forgotpasswordButton.clicked.connect(
            lambda: switchToWindow(Ui_ForgotPasswordWindow))
        
    # Ui_ForgotPasswordWindow buttons
    if type(ui) is Ui_ForgotPasswordWindow:
        ui.cancelButton.clicked.connect(
            lambda: switchToWindow(Ui_MainWindow))
        ui.resetPasswordButton.clicked.connect(
            lambda:resetPasswordButtonClicked(ui,conn,cursor)
        )
        
    # Ui_ChangePasswordWindow
    if type(ui) is Ui_ChangePasswordWindow:
        # Hide the security question if the user is an admin
        if currentUser=='admin':
            ui.questionComboBox.hide()
            ui.answerLineEdit.hide()
            ui.label_5.hide()
        ui.cancelButton.clicked.connect(
            lambda: switchToWindow(Ui_LoggedWindow,currentUser))
        ui.changePasswordButton.clicked.connect(
            lambda:changePasswordButtonClicked(ui,conn,cursor,currentUser)
        )
        
    # Ui_GroupWindow buttons
    if type(ui) is Ui_GroupWindow:
        
        if currentUser!="admin":
            ui.deleteUserButton.hide()
        
        ui.usersConn=conn
        ui.usersCursor=cursor
        
        ui.displayGroupUsers(connGroup,cursorGroup,currentUser)
        
        ui.takeMeBackButton.clicked.connect(
            lambda: switchToWindow(Ui_LoggedWindow,currentUser,Ui_GroupWindow)
        )
        # prompt group name, insert into group database,parameters conn,cursor
        ui.newGroupButton.clicked.connect(
            lambda: newGroupButtonClicked(ui,connGroup,cursorGroup,currentUser)
        )
        ui.addToGroupButton.clicked.connect(
            lambda: addToGroupButtonClicked(ui,connGroup,cursorGroup,currentUser)
        )
        ui.leaveGroupButton.clicked.connect(
            lambda: leaveGroupButtonClicked(ui,connGroup,cursorGroup,currentUser)
        )
        ui.appointLeaderButton.clicked.connect(
            lambda: appointLeaderButtonClicked(ui,connGroup,cursorGroup,currentUser)
        )
        ui.removeFromGroupButton.clicked.connect(
            lambda: removeFromGroupButtonClicked(ui,connGroup,cursorGroup,currentUser)
        )
        ui.disbandGroupButton.clicked.connect(
            lambda: disbandGroupButtonClicked(ui,connGroup,cursorGroup,currentUser)
        )
        ui.deleteUserButton.clicked.connect(
            lambda: deleteUserButtonClicked(ui,conn,cursor,connGroup,cursorGroup)
        )


if __name__ == "__main__":
    try:
        dataLocation = os.environ['HOME']+"/KorData"
        os.mkdir(dataLocation)
        print("Data location succesfully created at",
              dataLocation)
    except FileExistsError:
        print("Cannot create KorData, directory already exists.")
    try:
        """start user database"""
        database_path = 'users.db'
        conn = sqlite3.connect(database_path)
        cursor = conn.cursor()
        
        """start group database"""
        group_database_path='groups.db'
        connGroup=sqlite3.connect(group_database_path)
        cursorGroup = connGroup.cursor()
        
        # Check if table exists,if not,create it
        cursor.execute(
            ''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='user_info' ''')
        if cursor.fetchone()[0] == 0:
            cursor.execute(
                ''' CREATE TABLE user_info (username text,
                                            password text,
                                            role text,
                                            directory text,
                                            secQuestion text,
                                            secAnswer text,
                                            UNIQUE(username))''')
            conn.commit()
            
        cursorGroup.execute(
            ''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='group_info' ''')
        if cursorGroup.fetchone()[0] == 0:
            cursorGroup.execute(
                ''' CREATE TABLE group_info (groupLeader text,
                                             groupName text,
                                             members text,
                                             UNIQUE(groupName))''')
            connGroup.commit()


        # Default admin account
        cursor.execute(
            ''' SELECT COUNT(*) FROM user_info WHERE username='admin' ''')
        if cursor.fetchone()[0] == 0:
            cursor.execute(
                "INSERT INTO user_info VALUES (?,?,?,?,?,?)", ('admin', EncryptLibrary.hashPassword('admin1!'), 'Admin', dataLocation, "", ""))
            conn.commit()

        """--------------------"""

        app = QtWidgets.QApplication(sys.argv)

        """ This needs to be in main only for the first page """
        MainWindow = QtWidgets.QMainWindow()

        ui = Ui_MainWindow()
        ui.setupUi(MainWindow)

        ui.loginButton.clicked.connect(
            lambda: loginButtonClicked(ui, switchToWindow, conn, cursor))

        ui.registerButton.clicked.connect(
            lambda: switchToWindow(Ui_RegisterWindow))

        ui.forgotpasswordButton.clicked.connect(
            lambda: switchToWindow(Ui_ForgotPasswordWindow))

        """Add more MainWindow related buttons above and in switchToWindow"""

        MainWindow.show()

        sys.exit(app.exec_())
    finally:
        print("Closing databases ...")
        conn.close()
        connGroup.close()
        print("Databases closed succesfully")
        print("Encrypting files ...")
        EncryptLibrary.encryptFiles(dataLocation)
        