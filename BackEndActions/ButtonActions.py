import sqlite3
from BackEndActions import EncryptLibrary


def loginButtonClicked(ceva=''):
    print(f"Login button clicked {ceva}")


def forgotpasswordButtonClicked(ceva=''):
    print(f"Forgot password button clicked {ceva}")


def registerButtonClicked(ui, conn=None, c=None):

    username = ui.usernameRegInput.text()
    password = ui.passwordRegInput.text()
    role = ui.roleRegSelect.currentText()
    confirmedPassword = ui.confirmRegPasswordInput.text()

    if EncryptLibrary.validUsername(username) is False:
        print("Username must be between 6-20 characters and \nmust contain only letters,numbers and underscores")
    elif EncryptLibrary.validPassword(password) is False:
        print("Password must be between 6-20 characters and \nmust contain a letter,a number and a special character")
    elif password != confirmedPassword:
        print("Password does not match")
    else:
        # Use values as tuple,secure
        tmp = (username, EncryptLibrary.hashPassword(password), role)
        try:
            c.execute("INSERT INTO user_info VALUES (?,?,?)", tmp)
            for row in c.execute("SELECT * FROM user_info"):
                print('\t', row)
        except sqlite3.IntegrityError:  # if user is already taken
            print("Username already taken")
        conn.commit()
