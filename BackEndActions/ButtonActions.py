import sqlite3
from BackEndActions import EncryptLibrary


def loginButtonClicked(ceva=''):
    print(f"Login button clicked {ceva}")


def forgotpasswordButtonClicked(ceva=''):
    print(f"Forgot password button clicked {ceva}")


def registerButtonClicked(ui, conn=None, c=None):

    username = ui.usernameRegInput.text()
    password = ui.passwordRegInput.text()

    # Use values as tuple,secure
    tmp = (username, EncryptLibrary.hashPassword(password), None)
    try:
        c.execute("INSERT INTO user_info VALUES (?,?,?)", tmp)
        for row in c.execute("SELECT * FROM user_info"):
            print('\t', row)
    except sqlite3.IntegrityError:  # if user is already taken
        print("Username already taken")
    conn.commit()
