#!/usr/bin/python3
from PyQt5 import QtWidgets

from UserInterface.mainPage import Ui_MainWindow
from UserInterface.registerPage import Ui_RegisterWindow
from UserInterface.loggedPage import Ui_LoggedWindow
from UserInterface.forgotPasswordPage import Ui_ForgotPasswordWindow
from UserInterface.changePassword import Ui_ChangePasswordWindow
from UserInterface.groupPage import Ui_GroupWindow
from BackEndActions.ButtonActions import *
from BackEndActions.EncryptLibrary import *

import sys
import os
import sqlite3
import subprocess
import unittest


class TestEncryptLibraryMethods(unittest.TestCase):

    def test_verify_password(self):
        password = hashPassword("SamplePassword")

        self.assertTrue(verifyPassword(password, "SamplePassword"))
        self.assertFalse(verifyPassword(password, "WrongPassword"))

    def test_valid_password(self):
        self.assertTrue(validPassword("qwerty1!"))
        self.assertFalse(validPassword("notagoodpassword"))

    def test_valid_username(self):
        self.assertTrue(validUsername("foo.bar"))
        self.assertTrue(validUsername("admin"))
        self.assertTrue(validUsername("twentycharacterslong"))
        self.assertFalse(validPassword("_badusername"))


class TestDirectoryLocation(unittest.TestCase):
    def test_directory_location(self):
        dataLocation = os.environ['HOME']+"/.KorData"
        self.assertTrue(os.path.exists(dataLocation))


class TestWindowsSizes(unittest.TestCase):
    def test_Ui_MainWindow_size(self):
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        ui = Ui_MainWindow()
        ui.setupUi(MainWindow)
        MainWindow.show()

        self.assertEqual(MainWindow.frameSize().width(), 730)
        self.assertEqual(MainWindow.frameSize().height(), 730)

    def test_Ui_RegisterWindow_size(self):
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        ui = Ui_RegisterWindow()
        ui.setupUi(MainWindow)
        MainWindow.show()

        self.assertEqual(MainWindow.frameSize().width(), 730)
        self.assertEqual(MainWindow.frameSize().height(), 730)

    def test_Ui_ForgotPasswordWindow_size(self):
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        ui = Ui_ForgotPasswordWindow()
        ui.setupUi(MainWindow)
        MainWindow.show()

        self.assertGreater(MainWindow.frameSize().width(),
                           730, 'incorrect window size')
        self.assertEqual(MainWindow.frameSize().height(), 730)


class TestForExistingGuests(unittest.TestCase):
    def test_if_guests_not_deleted(self):
        absolute_path = sys.path[0]

        database_path = absolute_path+'/users.db'
        conn = sqlite3.connect(database_path)
        cursor = conn.cursor()

        maximumTime = 8

        cursor.execute(
            '''SELECT username,CAST((julianday(DATETIME(\"now\"))
             - julianday(dateCreated))*24 AS real) AS TimeOffInHours 
             FROM user_info WHERE role=\"Guest\"''')
        for row in cursor.fetchall():
            guestName = row[0]
            timeRemaining = maximumTime-float(row[1])

            self.assertGreater(timeRemaining, 0)


class TestFileEncryption(unittest.TestCase):
    def test_file_encryption(self):
        absolute_path = sys.path[0]
        os.mkdir(absolute_path+"/Testing")
        subprocess.run(
            ['touch', absolute_path+"/Testing/somefile.txt"], check=True)
        EncryptLibrary.encryptFiles(absolute_path+"/Testing")

        self.assertTrue(os.path.isfile(
            absolute_path+"/Testing/somefile.txt.aes"))
        os.remove(absolute_path+"/Testing/somefile.txt.aes")
        os.rmdir(absolute_path+"/Testing")

    def test_file_decryption(self):
        absolute_path = sys.path[0]
        os.mkdir(absolute_path+"/Testing")
        subprocess.run(
            ['touch', absolute_path+"/Testing/somefile.txt"], check=True)
        EncryptLibrary.encryptFiles(absolute_path+"/Testing")
        EncryptLibrary.encryptFiles(absolute_path+"/Testing", decrypt=True)

        self.assertTrue(os.path.isfile(
            absolute_path+"/Testing/somefile.txt"))
        os.remove(absolute_path+"/Testing/somefile.txt")
        os.rmdir(absolute_path+"/Testing")


if __name__ == '__main__':
    unittest.main()
