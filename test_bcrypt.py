# coding:utf-8
import unittest

import flask
from flask_bcrypt import (Bcrypt,
                          check_password_hash,
                          generate_password_hash,
                          PY3)


class BasicTestCase(unittest.TestCase):

    def setUp(self):
        app = flask.Flask(__name__)
        app.config['BCRYPT_LOG_ROUNDS'] = 6
        app.config['BCRYPT_HASH_IDENT'] = '2b'
        app.config['BCRYPT_HANDLE_LONG_PASSWORDS'] = False
        self.bcrypt = Bcrypt(app)

    def test_is_string(self):
        pw_hash = self.bcrypt.generate_password_hash('secret')
        if PY3:
            self.assertTrue(isinstance(pw_hash, bytes))
        else:
            self.assertTrue(isinstance(pw_hash, str))

    def test_custom_rounds(self):
        password = 'secret'
        pw_hash1 = self.bcrypt.generate_password_hash(password, 5)
        self.assertNotEqual(password, pw_hash1)

    def test_check_hash(self):
        pw_hash = self.bcrypt.generate_password_hash('secret')
        # check a correct password
        self.assertTrue(self.bcrypt.check_password_hash(pw_hash, 'secret'))
        # check an incorrect password
        self.assertFalse(self.bcrypt.check_password_hash(pw_hash, 'hunter2'))
        # check unicode
        pw_hash = self.bcrypt.generate_password_hash(u'\u2603')
        self.assertTrue(self.bcrypt.check_password_hash(pw_hash, u'\u2603'))
        # check helpers
        pw_hash = generate_password_hash('hunter2')
        self.assertTrue(check_password_hash(pw_hash, 'hunter2'))

    def test_check_hash_unicode_is_utf8(self):
        password = u'\u2603'
        pw_hash = self.bcrypt.generate_password_hash(password)
        # check a correct password
        self.assertTrue(self.bcrypt.check_password_hash(pw_hash, b'\xe2\x98\x83'))

    def test_rounds_set(self):
        self.assertEqual(self.bcrypt._log_rounds, 6)

    def test_unicode_hash(self):
        password = u'東京'
        h = generate_password_hash(password).decode('utf-8')
        self.assertTrue(check_password_hash(h, password))

    def test_long_password(self):
        """Test bcrypt maximum password length.

        The bcrypt algorithm has a maximum password length of 72 bytes, and
        ignores any bytes beyond that."""

        # Create a password with a 72 bytes length
        password = 'A' * 72
        pw_hash = self.bcrypt.generate_password_hash(password)
        # Ensure that a longer password yields the same hash
        self.assertTrue(self.bcrypt.check_password_hash(pw_hash, 'A' * 80))


class LongPasswordsTestCase(BasicTestCase):

    def setUp(self):
        app = flask.Flask(__name__)
        app.config['BCRYPT_LOG_ROUNDS'] = 6
        app.config['BCRYPT_HASH_IDENT'] = '2b'
        app.config['BCRYPT_HANDLE_LONG_PASSWORDS'] = True
        self.bcrypt = Bcrypt(app)

    def test_long_password(self):
        """Test the work around bcrypt maximum password length."""

        # Create a password with a 72 bytes length
        password = 'A' * 72
        pw_hash = self.bcrypt.generate_password_hash(password)
        # Ensure that a longer password **do not** yield the same hash
        self.assertFalse(self.bcrypt.check_password_hash(pw_hash, 'A' * 80))


if __name__ == '__main__':
    unittest.main()
