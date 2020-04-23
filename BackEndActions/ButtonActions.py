import sqlite3
from BackEndActions import EncryptLibrary


def loginButtonClicked(ui, conn=None, c=None):
    # TODO: pass switchToWindow function
    username = ui.usernameInput.text()
    providedPassword = ui.passwordInput.text()

    # Stripping username of white spaces
    if username.strip() and username.strip() != 'None':
        res = c.execute('''SELECT password 
                        FROM user_info
                        WHERE username=? ''',
                        (username, ))
        storedPassword = res.fetchone()[0]

        if EncryptLibrary.verifyPassword(storedPassword, providedPassword):
            print("Logged in as", username)
        else:
            print("Invalid username or password")
    else:
        print("Invalid username or password")


def forgotpasswordButtonClicked(ui, conn, c):
    for row in c.execute("SELECT * FROM user_info"):
        print('\t', row[0], row[1])


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
        except sqlite3.IntegrityError:  # if user is already taken
            print("Username already taken")
        conn.commit()
