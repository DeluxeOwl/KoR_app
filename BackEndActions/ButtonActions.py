import sqlite3
import os
import subprocess
from BackEndActions import EncryptLibrary
from UserInterface.mainPage import Ui_MainWindow
from UserInterface.dashboard import Ui_LoggedWindow
from UserInterface.forgotPasswordPage import Ui_ForgotPasswordWindow
from PyQt5 import QtCore,QtWidgets
from PyQt5.QtWidgets import QMessageBox
from UserInterface.dialog import Ui_Dialog


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

    username = ui.usernameLineEdit.text()
    newPassword = ui.newPasswordLineEdit.text()
    confirmedPassword = ui.confirmLineEdit.text()
    
    secQuestion=ui.questionComboBox.currentText()
    
    answer=ui.answerLineEdit.text()
    
    if not EncryptLibrary.validUsername(username) or not EncryptLibrary.validPassword(newPassword):
        clickMethod(ui.resetPasswordButton,"Invalid username or password")
    elif newPassword!=confirmedPassword:
        clickMethod(ui.resetPasswordButton,"Passwords do not match")
    else:
        # select the username,check if it exists,then check if the secQ matches
        c.execute(
            "SELECT secQuestion,secAnswer FROM user_info WHERE username=?",(username,))
        
        try:
            response = c.fetchall()[0]
            secQuestionDB = response[0]
            secAnswerDB = response[1]
        except:
            response=None
            clickMethod(ui.resetPasswordButton,"Invalid username")
            return

            
        if secQuestionDB!=secQuestion:
            clickMethod(ui.resetPasswordButton,"Invalid question or answer")
        elif EncryptLibrary.verifyPassword(secAnswerDB,answer):
            c.execute(
                "UPDATE user_info SET password=? WHERE username=?",(EncryptLibrary.hashPassword(newPassword),username))
            conn.commit()
            clickMethod(ui.resetPasswordButton,"Password changed succesfully!")
        else:
            clickMethod(ui.resetPasswordButton,"Invalid question or answer")
            
def changePasswordButtonClicked(ui,conn=None,c=None,currentUser=None):

    username = currentUser
    newPassword = ui.newPasswordLineEdit.text()
    confirmedPassword = ui.confirmLineEdit.text()
    
    if currentUser!='admin':
        secQuestion=ui.questionComboBox.currentText()
        
        answer=ui.answerLineEdit.text()
        
        if not EncryptLibrary.validPassword(newPassword):
            clickMethod(ui.changePasswordButton,"Invalid password")
        elif newPassword!=confirmedPassword:
            clickMethod(ui.changePasswordButton,"Passwords do not match")
        else:
            # select the username,check if it exists,then check if the secQ matches
            c.execute(
                "SELECT secQuestion,secAnswer FROM user_info WHERE username=?",(username,))
            
            try:
                response = c.fetchall()[0]
                secQuestionDB = response[0]
                secAnswerDB = response[1]
            except:
                response=None
                clickMethod(ui.changePasswordButton,"CRITICAL ERROR")
                return

                
            if secQuestionDB!=secQuestion:
                clickMethod(ui.changePasswordButton,"Invalid question or answer")
            elif EncryptLibrary.verifyPassword(secAnswerDB,answer):
                c.execute(
                    "UPDATE user_info SET password=? WHERE username=?",(EncryptLibrary.hashPassword(newPassword),username))
                conn.commit()
                clickMethod(ui.changePasswordButton,"Password changed succesfully!")
            else:
                clickMethod(ui.changePasswordButton,"Invalid question or answer")
    else:
        if not EncryptLibrary.validPassword(newPassword):
            clickMethod(ui.changePasswordButton,"Invalid password")
        elif newPassword!=confirmedPassword:
            clickMethod(ui.changePasswordButton,"Passwords do not match")
        else:
            c.execute(
                    "UPDATE user_info SET password=? WHERE username=?",(EncryptLibrary.hashPassword(newPassword),username))
            conn.commit()
            clickMethod(ui.changePasswordButton,"Password changed succesfully!")
            
            
def newGroupButtonClicked(ui,conn=None,c=None,currentUser=None):
    dialog = QtWidgets.QDialog()
    dialog.ui = Ui_Dialog()
    dialog.ui.setupUi(dialog)
    dialog.setAttribute(QtCore.Qt.WA_DeleteOnClose)

    dialog.ui.changeText("Group name:")
    dialog.ui.pushButtonCancel.clicked.connect(dialog.done)

    def groupName():
        name = dialog.ui.getLineEditAnswer()
        tmp=(currentUser,name,currentUser)
        try:
            c.execute(
                "INSERT INTO group_info VALUES (?,?,?)",tmp
            )
            conn.commit()
            dialog.done(0)
            ui.displayGroupUsers(conn,c,currentUser)
        except sqlite3.IntegrityError:
            clickMethod(ui.newGroupButton,"Name already taken")
        
    
    dialog.ui.pushButtonOK.clicked.connect(groupName)

    dialog.exec_()
    
def addToGroupButtonClicked(ui,conn=None,c=None,currentUser=None):
    group = ui.groupComboBox.currentText()
    user = ui.userComboBox.currentText()
    
    c.execute("SELECT * FROM group_info WHERE groupName=?",(group,))
    
    for values in c.fetchall():
        groupLeader = values[0]
        groupName = values[1]
        members = values[2]
        
        if groupLeader !=currentUser:
            clickMethod(ui.addToGroupButton,"You don't have permission to do that")
        elif user in members.split():
            clickMethod(ui.addToGroupButton,"User already in group")
        else:
            members=members+" "+user
            c.execute("UPDATE group_info SET members=? WHERE groupName=?",(members,groupName))
            conn.commit()
    ui.displayGroupUsers(conn,c,currentUser)
    
def leaveGroupButtonClicked(ui,conn=None,c=None,currentUser=None):
    group = ui.groupComboBox.currentText()
    c.execute("SELECT * FROM group_info WHERE groupName=?",(group,))
    
    for values in c.fetchall():
        groupLeader = values[0]
        groupName = values[1]
        members = values[2]
        
        if currentUser not in members.split():
            clickMethod(ui.leaveGroupButton,"You're not part of that group")
        elif groupLeader==currentUser:
            clickMethod(ui.leaveGroupButton,"You must appoint a new leader before leaving the group")
        else:
            members=members.split()
            members.remove(currentUser)
            members = ' '.join(members)
            c.execute("UPDATE group_info SET members=? WHERE groupName=?",(members,groupName))
            conn.commit()
        
    ui.displayGroupUsers(conn,c,currentUser)  

def appointLeaderButtonClicked(ui,conn=None,c=None,currentUser=None):
    group = ui.groupComboBox.currentText()
    user = ui.userComboBox.currentText()
    
    c.execute("SELECT * FROM group_info WHERE groupName=?",(group,))
    
    for values in c.fetchall():
        groupLeader = values[0]
        groupName = values[1]
        members = values[2]
        
        if currentUser!=groupLeader:
            clickMethod(ui.appointLeaderButton,"You're not the leader of this group")
        elif user not in members.split():
            clickMethod(ui.appointLeaderButton,"The user is not part of this group")
        else:
            c.execute("UPDATE group_info SET groupLeader=? WHERE groupName=?",(user,groupName))
            conn.commit()
    
    ui.displayGroupUsers(conn,c,currentUser) 
            
def removeFromGroupButtonClicked(ui,conn=None,c=None,currentUser=None):
    group = ui.groupComboBox.currentText()
    user = ui.userComboBox.currentText()
    
    c.execute("SELECT * FROM group_info WHERE groupName=?",(group,))
    
    for values in c.fetchall():
        groupLeader = values[0]
        groupName = values[1]
        members = values[2]
        
        if currentUser!=groupLeader:
            clickMethod(ui.appointLeaderButton,"You're not the leader of this group")
        elif user==currentUser:
            clickMethod(ui.appointLeaderButton,"If you wish to leave your group,appoint a new leader then press the \"Leave group\" button")
        elif user not in members.split():
            clickMethod(ui.appointLeaderButton,"The user is not part of this group")
        else:
            members=members.split()
            members.remove(user)
            members = ' '.join(members)
            c.execute("UPDATE group_info SET members=? WHERE groupName=?",(members,groupName))
            conn.commit()

    ui.displayGroupUsers(conn,c,currentUser) 