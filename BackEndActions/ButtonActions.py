import sqlite3
import os
import uuid
import hashlib
import binascii


def loginButtonClicked(ceva=''):
    print(f"Login button clicked {ceva}")


def registerButtonClicked(username='', password='', conn=None, c=None):

    def hashPassword(password):
        salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
        pwdhash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'),
                                      salt, 100000)  # 100k iterations
        pwdhash = binascii.hexlify(pwdhash)
        return (salt + pwdhash).decode('ascii')

    # Use values as tuple,secure
    tmp = (username, hashPassword(password))
    try:
        c.execute("INSERT INTO user_info VALUES (?,?)", tmp)
        for row in c.execute("SELECT * FROM user_info"):
            print('\t', row)
    except sqlite3.IntegrityError:  # if user is already taken
        print("Username already taken")

    conn.commit()
