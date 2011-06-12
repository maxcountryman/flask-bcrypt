This is a simple Flask extension that provides bcrypt support.

To use simply do the following:

    from flaskext.bcrypt import generate_password_hash, check_password_hash
    
    pw_hash = generate_password_hash('secret')
    
    check_password_hash(pw_hash, 'secret')
