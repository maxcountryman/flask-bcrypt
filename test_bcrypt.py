import unittest

import flask
from flaskext.bcrypt import Bcrypt


class BasicTestCase(unittest.TestCase):
    
    def setUp(self):
        app = flask.Flask(__name__)
        app.config['BCRYPT_LOG_ROUNDS'] = 6
        self.bcrypt = Bcrypt(app)
        
    def test_is_string(self):
        pw_hash = self.bcrypt.generate_password_hash('secret')
        self.assertTrue(isinstance(pw_hash, str))
        
    def test_not_string(self):
        pw_hash = self.bcrypt.generate_password_hash(42)
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
    
    def test_rounds_set(self):
        self.assertEquals(self.bcrypt._log_rounds, 6)


if __name__ == '__main__':
    unittest.main()

