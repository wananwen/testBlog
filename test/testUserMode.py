import unittest
from ..app.model.base import User


class UserModeTestCase(unittest.TestCase):
    def test_passwd_setter(self):
        u = User(passwd='Dog')
        self.assertTrue(u.passwd_hash is not None)

    def test_no_passwd_getter(self):
        u = User(passwd='Dog')
        with self.assertRaises(AttributeError):
            u.passwd

    def test_verity_passwd(self):
        u = User(passwd='Dog')
        self.assertTrue(u.verity_passwd('Dog'))
        self.assertFalse(u.verity_passwd('Cat'))

    def test_passwd_salts_are_random(self):
        u = User(passwd='Dog')
        u2 = User(passwd='Dog')
        self.assertFalse(u.passwd_hash == u2.passwd_hash)


if __name__ == "__main__":
    unittest.runner()
