import unittest
import sys
import flask

from flaskext.bcrypt import bcrypt_init, generate_password_hash, check_password_hash

class BasicTestCase(unittest.TestCase):
    
    def setUp(self):
        app = flask.Flask(__name__)
        app.config['BCRYPT_LOG_ROUNDS'] = 6
        bcrypt_init(app)
        self.password = 'secret'
        self.pw_hash = generate_password_hash(self.password)
        
    def test_is_string(self):
        self.assertTrue(isinstance(self.pw_hash, str))
        
    def test_not_string(self):
        pw_hash = generate_password_hash(42)
        self.assertTrue(isinstance(pw_hash, str))
        
    def test_custom_rounds(self):
        pw_hash = generate_password_hash(self.password, 5) # high values will be slow!
        self.assertTrue(isinstance(pw_hash, str))
        
    def test_check_hash(self):
        # check a correct password
        a = check_password_hash(self.pw_hash, 'secret')
        self.assertTrue(a)
        # check a wrong password
        b = check_password_hash(self.pw_hash, 'test')
        self.assertFalse(b)

    def test_check_hash_unicode(self):
        password=u'\u2603'
        x = generate_password_hash(password)
        # check a correct password
        a = check_password_hash(x, password)
        self.assertTrue(a)
        # check a wrong password
        b = check_password_hash(x, 'test')
        self.assertFalse(b)

    def test_check_hash_unicode_is_utf8(self):
        password=u'\u2603'
        x = generate_password_hash(password)
        # check a correct password
        a = check_password_hash(x, '\xe2\x98\x83')
        self.assertTrue(a)
    
    def test_rounds_set(self):
        self.assertTrue(sys.modules['flaskext.bcrypt']._log_rounds[0] == 6)

if __name__ == '__main__':
    unittest.main()

