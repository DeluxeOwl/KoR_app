#!/usr/bin/python3
from PyQt5 import QtWidgets

from UserInterface.mainPage import Ui_MainWindow
from UserInterface.registerPage import Ui_RegisterWindow
from UserInterface.loggedPage import Ui_LoggedWindow
from UserInterface.forgotPasswordPage import Ui_ForgotPasswordWindow
from UserInterface.changePassword import Ui_ChangePasswordWindow
from UserInterface.groupPage import Ui_GroupWindow
from BackEndActions.ButtonActions import *
from BackEndActions.EncryptLibrary import encryptFiles

import sys
import os
import sqlite3
import subprocess


def switchToWindow(windowToSwitchTo, currentUser=None, lastWindow=None):
    '''
    Switches to the window and acts as a controller for its buttons.
    Takes 2 optional arguments,the current user and the last window.
    Last window is used to get back from the groups window 
    '''

    # Get old window sizes,magic offset numbers
    newWidth = MainWindow.frameSize().width() - 8
    newHeight = MainWindow.frameSize().height() - 33

    # Make the window appear
    ui = windowToSwitchTo()
    ui.setupUi(MainWindow)
    MainWindow.show()

    # Adjust the size in case the user stretched the window
    MainWindow.resize(newWidth, newHeight)

    # Get the current UI
    currentUI = type(ui)

    '''
    Below are the controls for different windows
    We use lambdas to call the functions,because we can't connect with parameters
    '''

    # Ui_RegisterWindow buttons
    if currentUI is Ui_RegisterWindow:
        ui.cancelRegButton.clicked.connect(
            lambda: switchToWindow(Ui_MainWindow))
        ui.signUpRegButton.clicked.connect(
            lambda: registerButtonClicked(ui, switchToWindow, dataLocation, conn, cursor))

    # Ui_LoggedWindow buttons
    if currentUI is Ui_LoggedWindow:
        ui.labelUsername.setText(currentUser)

        # We set the user's directory
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
            lambda: logoutButtonClicked(switchToWindow, currentUser, conn, cursor, connGroup, cursorGroup))
        ui.pushButtonOpenFiles.clicked.connect(
            lambda: pushButtonOpenFilesClicked(ui, currentUser, conn, cursor)
        )
        ui.pushButtonChangePassword.clicked.connect(
            lambda: switchToWindow(Ui_ChangePasswordWindow, currentUser)
        )
        ui.pushButtonGroups.clicked.connect(
            lambda: switchToWindow(Ui_GroupWindow, currentUser)
        )

    # Ui_MainWindow buttons
    if currentUI is Ui_MainWindow:
        ui.loginButton.clicked.connect(
            lambda: loginButtonClicked(ui, switchToWindow, conn, cursor))

        ui.registerButton.clicked.connect(
            lambda: switchToWindow(Ui_RegisterWindow))

        ui.forgotpasswordButton.clicked.connect(
            lambda: switchToWindow(Ui_ForgotPasswordWindow))

    # Ui_ForgotPasswordWindow buttons
    if currentUI is Ui_ForgotPasswordWindow:
        ui.cancelButton.clicked.connect(
            lambda: switchToWindow(Ui_MainWindow))
        ui.resetPasswordButton.clicked.connect(
            lambda: resetPasswordButtonClicked(ui, conn, cursor)
        )

    # Ui_ChangePasswordWindow
    if currentUI is Ui_ChangePasswordWindow:
        # Hide the security question if the user is an admin
        if currentUser == 'admin':
            ui.questionComboBox.hide()
            ui.answerLineEdit.hide()
            ui.label_5.hide()
        ui.cancelButton.clicked.connect(
            lambda: switchToWindow(Ui_LoggedWindow, currentUser))
        ui.changePasswordButton.clicked.connect(
            lambda: changePasswordButtonClicked(ui, conn, cursor, currentUser)
        )

    # Ui_GroupWindow buttons
    if currentUI is Ui_GroupWindow:

        if currentUser != "admin":
            ui.deleteUserButton.hide()

        ui.usersConn = conn
        ui.usersCursor = cursor

        ui.displayGroupUsers(connGroup, cursorGroup, currentUser)

        ui.takeMeBackButton.clicked.connect(
            lambda: switchToWindow(
                Ui_LoggedWindow, currentUser, Ui_GroupWindow)
        )
        ui.newGroupButton.clicked.connect(
            lambda: newGroupButtonClicked(
                ui, connGroup, cursorGroup, currentUser)
        )
        ui.addToGroupButton.clicked.connect(
            lambda: addToGroupButtonClicked(
                ui, connGroup, cursorGroup, currentUser)
        )
        ui.leaveGroupButton.clicked.connect(
            lambda: leaveGroupButtonClicked(
                ui, connGroup, cursorGroup, currentUser)
        )
        ui.appointLeaderButton.clicked.connect(
            lambda: appointLeaderButtonClicked(
                ui, connGroup, cursorGroup, currentUser)
        )
        ui.removeFromGroupButton.clicked.connect(
            lambda: removeFromGroupButtonClicked(
                ui, connGroup, cursorGroup, currentUser)
        )
        ui.disbandGroupButton.clicked.connect(
            lambda: disbandGroupButtonClicked(
                ui, connGroup, cursorGroup, currentUser)
        )
        ui.deleteUserButton.clicked.connect(
            lambda: deleteUserButtonClicked(
                ui, conn, cursor, connGroup, cursorGroup)
        )
        ui.openFilesButton.clicked.connect(
            lambda: openFilesButtonClicked(
                ui, connGroup, cursorGroup, currentUser)
        )


def checkForGuests(conn, cursor, connGroup, cursorGroup):

    # time in hours
    maximumTime = 8

    # Get all the guests and the time since registration
    cursor.execute(
        "SELECT username,CAST((julianday(DATETIME(\"now\")) - julianday(dateCreated))*24 AS real) AS TimeOffInHours FROM user_info WHERE role=\"Guest\"")
    for row in cursor.fetchall():
        guestName = row[0]
        timeRemaining = maximumTime-float(row[1])

        if timeRemaining <= 0:

            # Deleting from the users database
            cursor.execute(
                "SELECT * FROM user_info WHERE username=?", (guestName,))
            for first_row in cursor.fetchall():
                userDirectory = first_row[3]
                print("Deleting directory", userDirectory)
                subprocess.run(['rm', '-rf', userDirectory], check=True)

                cursor.execute(
                    "DELETE FROM user_info WHERE username=?", (guestName,))

                conn.commit()

            # Deleting from the groups database
            cursorGroup.execute(
                "DELETE FROM group_info WHERE groupLeader=?", (guestName,))
            connGroup.commit()

            cursorGroup.execute("SELECT * FROM group_info")

            for values in cursorGroup.fetchall():
                groupName = values[1]
                members = values[2]

                members = members.split()
                if guestName in members:
                    members.remove(guestName)
                    members = ' '.join(members)
                    cursorGroup.execute(
                        "UPDATE group_info SET members=? WHERE groupName=?", (members, groupName))
                    connGroup.commit()


if __name__ == "__main__":

    try:
        dataLocation = os.environ['HOME']+"/.KorData"
        os.mkdir(dataLocation)
        print("Data location succesfully created at",
              dataLocation)
    except FileExistsError:
        print("Cannot create KorData, directory already exists.")
    try:
        '''Start the user database connection'''
        absolute_path = sys.path[0]
        database_path = absolute_path+'/users.db'
        conn = sqlite3.connect(database_path)
        cursor = conn.cursor()

        '''Start the group database connection'''
        group_database_path = absolute_path+'/groups.db'
        connGroup = sqlite3.connect(group_database_path)
        cursorGroup = connGroup.cursor()

        # Check if user_info table exists,if not,create it
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
                                            dateCreated text,
                                            UNIQUE(username))''')
            conn.commit()

        # Check if group_info table exists,if not,create it
        cursorGroup.execute(
            ''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='group_info' ''')
        if cursorGroup.fetchone()[0] == 0:
            cursorGroup.execute(
                ''' CREATE TABLE group_info (groupLeader text,
                                             groupName text,
                                             members text,
                                             UNIQUE(groupName))''')
            connGroup.commit()

        # Insert the default admin:admin1! account,password should be changed later
        cursor.execute(
            ''' SELECT COUNT(*) FROM user_info WHERE username='admin' ''')
        if cursor.fetchone()[0] == 0:
            cursor.execute(
                "INSERT INTO user_info VALUES (?,?,?,?,?,?,DATETIME(\"now\"))", ('admin', EncryptLibrary.hashPassword('admin1!'), 'Admin', dataLocation, "", "",))
            conn.commit()

        # Check for guest accounts that are overdue and delete them
        checkForGuests(conn, cursor, connGroup, cursorGroup)
        app = QtWidgets.QApplication(sys.argv)

        '''We display the main page'''
        MainWindow = QtWidgets.QMainWindow()

        switchToWindow(Ui_MainWindow)

        sys.exit(app.exec_())
    finally:
        print("Closing databases ...")
        # Check for guest accounts that are overdue and delete on exit
        checkForGuests(conn, cursor, connGroup, cursorGroup)

        # Close the database connections
        conn.close()
        connGroup.close()
        print("Databases closed succesfully")

        # Encrypt the files at exit
        EncryptLibrary.encryptFiles(dataLocation)
