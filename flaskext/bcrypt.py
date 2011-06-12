from __future__ import absolute_import
import bcrypt


def generate_password_hash(password):
    '''Generates a password hash using `bcrypt`.
    
    Returns a tuple containing the hashed password and salt.
    '''
    
    if not password:
        raise ValueError('Password must be non-empty.')
    
    password = str(password)
    salt = bcrypt.gensalt()
    h = bcrypt.hashpw(password, salt)
    
    return (h, salt)


def check_password_hash(pw_hash, password):
    '''Checks a password hash and salt against a password. The password hash,
    `pw_hash` should be a tuple, containing the hash value `pw_hash[0]` and the
    salt `pw_hash[1]`.
    
    Returns `True` if the password matched, `False` otherwise.
    '''
    
    if len(pw_hash) != 2:
        raise ValueError('pw_hash must be two elements exactly.')
    
    hash_value, salt = pw_hash[0], pw_hash[1]
    
    return bcrypt.hashpw(password, salt) == hash_value

