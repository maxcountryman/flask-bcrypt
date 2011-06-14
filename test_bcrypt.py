from __future__ import with_statement

import unittest
import flask

from flaskext.bcrypt import generate_password_hash, check_password_hash

class BasicTestCase(unittest.TestCase):
    
    def setUp(self):
        password = 'secret'
        self.pw_hash = generate_password_hash(password)
        
    def test_is_tuple(self):
        self.assertTrue(isinstance(self.pw_hash, tuple))
        
    def test_not_string(self):
        pw_hash = generate_password_hash(42)
        self.assertTrue(isinstance(pw_hash[0], str))
        self.assertTrue(isinstance(pw_hash[1], str))
        
    def test_custom_rounds(self):
        pw_hash = generate_password_hash('secret', 10) # high values will be slow!
        self.assertTrue(isinstance(pw_hash, tuple))
        
    def test_check_hash(self):
        # check a correct password
        a = check_password_hash(self.pw_hash, 'secret')
        self.assertTrue(a)
        # check a wrong password
        b = check_password_hash(self.pw_hash, 'test')
        self.assertFalse(b)

if __name__ == '__main__':
    unittest.main()

