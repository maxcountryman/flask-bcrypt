from __future__ import absolute_import
import bcrypt

_log_rounds = 12

def bcrypt_init(app):
    rounds = app.config.get('BCRYPT_LOG_ROUNDS', None)
    if rounds:
        _log_rounds = rounds

def generate_password_hash(password, rounds=_log_rounds):
    '''Generates a password hash using `bcrypt`. Specifying `log_rounds` sets 
    the log_rounds parameter of `bcrypt.gensalt()` which determines the 
    complexity of the salt. 12 is the default value.
    
    Returns the hashed password.
    '''
    
    if not password:
        raise ValueError('Password must be non-empty.')
    
    password = str(password)
    
    pw_hash = bcrypt.hashpw(password, bcrypt.gensalt(rounds))
    
    return pw_hash

def check_password_hash(pw_hash, password):
    '''Checks a hashed password against a password.
    
    Returns `True` if the password matched, `False` otherwise.
    '''
    
    return bcrypt.hashpw(password, pw_hash) == pw_hash

