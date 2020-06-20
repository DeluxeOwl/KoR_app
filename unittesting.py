import unittest
import os
from BackEndActions.EncryptLibrary import *


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


if __name__ == '__main__':
    unittest.main()
