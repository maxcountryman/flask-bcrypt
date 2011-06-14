This is a simple Flask extension that provides bcrypt support. The intention 
of this extension is to provide for stronger password hashing. Two functions 
are provided to override the werkzeug.security hashing functions.


To use, simply do the following:

    from flaskext.bcrypt import bcrypt_init, generate_password_hash, 
    check_password_hash
    
    bcrypt_init(app)
    
    pw_hash = generate_password_hash('secret')
    check_password_hash(pw_hash, 'secret')
