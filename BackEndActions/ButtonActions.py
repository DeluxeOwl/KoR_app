import sqlite3
import os
import subprocess
from BackEndActions import EncryptLibrary
from UserInterface.mainPage import Ui_MainWindow
from UserInterface.dashboard import Ui_LoggedWindow
from UserInterface.forgotPasswordPage import Ui_ForgotPasswordWindow
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


def registerButtonClicked(ui, switchBack, dataLocation, conn=None, c=None):

    username = ui.usernameRegInput.text()
    password = ui.passwordRegInput.text()

    secQuestion = ui.comboBoxSecurityQuestion.currentText()
    secAnswer = EncryptLibrary.hashPassword(ui.lineEditSecurityAnswer.text())

    role = ui.roleRegSelect.currentText()
    confirmedPassword = ui.confirmRegPasswordInput.text()

    if EncryptLibrary.validUsername(username) is False:
        print("Username must be between 6-20 characters and \nmust contain only letters,numbers and underscores")
        clickMethod(ui.signUpRegButton,
                    "Username must be between 6-20 characters and \nmust contain only letters,numbers and underscores")
    elif EncryptLibrary.validPassword(password) is False:
        print("Password must be between 6-20 characters and \nmust contain a letter,a number and a special character")
        clickMethod(ui.signUpRegButton,
                    "Password must be between 6-20 characters and \nmust contain a letter,a number and a special character")
    elif password != confirmedPassword:
        print("Password does not match")
        clickMethod(ui.signUpRegButton, "Password does not match")
    else:
        # Use values as tuple,secure
        dirLocation = dataLocation+"/"+username
        os.mkdir(dirLocation)
        tmp = (username, EncryptLibrary.hashPassword(
            password), role, dirLocation, secQuestion, secAnswer)
        try:
            c.execute("INSERT INTO user_info VALUES (?,?,?,?,?,?)", tmp)
            switchBack(Ui_MainWindow)
        except sqlite3.IntegrityError:  # if user is already taken
            print("Username already taken")
            clickMethod(ui.signUpRegButton, "Username already taken")
        conn.commit()


def logoutButtonClicked(switchBack, userLoggedOut, conn=None, c=None):
    switchBack(Ui_MainWindow)
    print("Logged out", userLoggedOut)

    c.execute("SELECT directory FROM user_info WHERE username=?",
              (userLoggedOut,))
    userDirectory = c.fetchone()[0]

    # Encrypt when logging out
    EncryptLibrary.encryptFiles(userDirectory)


def pushButtonOpenFilesClicked(ui, currentUser, conn=None, c=None):
    c.execute("SELECT directory FROM user_info WHERE username=?", (currentUser,))
    userDirectory = c.fetchone()[0]
    try:
        subprocess.run(['xdg-open', userDirectory], check=True)
    except subprocess.CalledProcessError:
        print("Error while opening.")


def clickMethod(self, msg):
    QMessageBox.about(self, "Warning", msg)
    
def resetPasswordButtonClicked(ui,conn=None,c=None):
    """
    verify that all fields are valid
    
    Take the username
    verify that it exists in the database
    check that the password matches
    check the security question and answer
    hash the password and update the database"""
    
    username = ui.usernameLineEdit.text()
    newPassword = ui.newPasswordLineEdit.text()
    confirmedPassword = ui.confirmLineEdit.text()
    
    secQuestion=ui.questionComboBox.currentText()
    
    answer=ui.answerLineEdit.text()
    
    print(username,newPassword,confirmedPassword,secQuestion,answer)
    
