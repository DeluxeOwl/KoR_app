import uuid
import hashlib
import binascii
import os
import re


def hashPassword(password):
    salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
    pwdhash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'),
                                  salt, 100000)  # 100k iterations
    pwdhash = binascii.hexlify(pwdhash)
    return (salt + pwdhash).decode('ascii')


def verifyPassword(storedPassword, providedPassword):
    salt = storedPassword[:64]
    storedPassword = storedPassword[64:]
    passwordHash = hashlib.pbkdf2_hmac('sha512',
                                       providedPassword.encode('utf-8'),
                                       salt.encode('ascii'),
                                       100000)
    passwordHash = binascii.hexlify(passwordHash).decode('ascii')

    return passwordHash == storedPassword


def validPassword(password):
    # between 6-20 characters,at least one letter,one number,one special symbol
    pattern = re.compile(
        "^(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{6,20}$")
    if re.search(pattern, password):
        return True
    else:
        return False


def validUsername(username):
    # 6-20 characters long,no _ or . at beginning,no __ _. ._ .. inside,allowed characters,no _ . at end
    pattern = re.compile(
        "^(?=.{6,20}$)(?![_.])(?!.*[_.]{2})[a-zA-Z0-9._]+(?<![_.])$")
    if re.search(pattern, username):
        return True
    else:
        return False
