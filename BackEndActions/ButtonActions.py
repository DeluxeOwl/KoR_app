import sqlite3
from BackEndActions import EncryptLibrary
from UserInterface.mainPage import Ui_MainWindow
from UserInterface.dashboard import Ui_LoggedWindow
from PyQt5 import QtCore
from PyQt5.QtWidgets import QMessageBox


def loginButtonClicked(ui, switchBack, conn=None, c=None):
    username = ui.usernameInput.text()
    providedPassword = ui.passwordInput.text()

    # Stripping username of white spaces
    if EncryptLibrary.validUsername(username) and EncryptLibrary.validPassword(providedPassword):
        res = c.execute('''SELECT password
                        FROM user_info
                        WHERE username=? ''',
                        (username, ))

        try:
            storedPassword = res.fetchone()[0]
            if EncryptLibrary.verifyPassword(storedPassword, providedPassword):
                print("Logged in as", username)
                switchBack(Ui_LoggedWindow, username)
            else:
                clickMethod(ui.loginButton, "Invalid username or password")
                print("Invalid username or password")
        except TypeError:
            clickMethod(ui.loginButton, "Invalid username or password")
            print("Invalid username or password")

    else:
        clickMethod(ui.loginButton, "Invalid username or password")
        print("Invalid username or password")


def forgotpasswordButtonClicked(ui, conn, c):
    for row in c.execute("SELECT * FROM user_info"):
        print('\t', row[0], row[1])


def registerButtonClicked(ui, switchBack, conn=None, c=None):

    username = ui.usernameRegInput.text()
    password = ui.passwordRegInput.text()
    role = ui.roleRegSelect.currentText()
    confirmedPassword = ui.confirmRegPasswordInput.text()

    if EncryptLibrary.validUsername(username) is False:
        print("Username must be between 6-20 characters and \nmust contain only letters,numbers and underscores")
        clickMethod(ui.signUpRegButton, "Username must be between 6-20 characters and \nmust contain only letters,numbers and underscores")
    elif EncryptLibrary.validPassword(password) is False:
        print("Password must be between 6-20 characters and \nmust contain a letter,a number and a special character")
        clickMethod(ui.signUpRegButton, "Password must be between 6-20 characters and \nmust contain a letter,a number and a special character")
    elif password != confirmedPassword:
        print("Password does not match")
        clickMethod(ui.signUpRegButton, "Password does not match")
    else:
        # Use values as tuple,secure
        tmp = (username, EncryptLibrary.hashPassword(password), role)
        try:
            c.execute("INSERT INTO user_info VALUES (?,?,?)", tmp)
            switchBack(Ui_MainWindow)
        except sqlite3.IntegrityError:  # if user is already taken
            print("Username already taken")
            clickMethod(ui.signUpRegButton, "Username already taken")
        conn.commit()


def logoutButtonClicked(switchBack):
    switchBack(Ui_MainWindow)
    print("Logged out")


def pushButtonOpenFilesClicked(ui):
    print("Open files clicked")

def clickMethod(self, msg):
    QMessageBox.about(self, "Warning", msg)