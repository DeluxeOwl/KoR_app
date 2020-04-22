import sqlite3
import os


def loginButtonClicked(ceva=''):
    print(f"Login button clicked {ceva}")


def registerButtonClicked(username='', password='', conn=None, c=None):
    # Use values as tuple,secure
    tmp = (username, password)
    try:
        c.execute("INSERT INTO user_info VALUES (?,?)", tmp)
        for row in c.execute("SELECT * FROM user_info"):
            print('\t', row)
    except sqlite3.IntegrityError:
        print("Username already taken")
    conn.commit()
