from __future__ import absolute_import
import bcrypt


def generate_password_hash(password, rounds=12):
    '''Generates a password hash using `bcrypt`. Specifying `rounds` sets the
    log_rounds parameter of `bcrypt.gensalt()` which determines the complexity
    of the salt. 12 is the default value, 4 is the minimum, and 31 maximum. 
    Ints exceeding 31 will be treated as if they were 31.
    
    Returns a string containing the hashed password.
    '''
    
    if not password:
        raise ValueError('Password must be non-empty.')
    
    password = str(password)
    
    salt = bcrypt.gensalt(rounds)
    h = bcrypt.hashpw(password, salt)
    
    return h
 

def check_password_hash(pw_hash, password):
    '''Checks a password hash and salt against a password. The password hash,
    `pw_hash` should be a string containing the previously hashed password.
    
    Returns `True` if the password matched, `False` otherwise.
    '''
    
    return bcrypt.hashpw(password, pw_hash) == pw_hash
