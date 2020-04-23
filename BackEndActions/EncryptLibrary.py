import uuid
import hashlib
import binascii
import os


def hashPassword(password):
    salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
    pwdhash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'),
                                  salt, 100000)  # 100k iterations
    pwdhash = binascii.hexlify(pwdhash)
    return (salt + pwdhash).decode('ascii')
