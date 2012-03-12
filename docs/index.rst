Flask-Bcrypt
=============

.. module:: flaskext.bcrypt

Flask-Bcrypt is a Flask extension that provides bcrypt hashing utilities for
your application.

Due to the recent increased prevelance of powerful hardware, such as modern
GPUs, hashes have become increasingly easy to crack. A proactive solution to
this is to use a hash that was designed to be "de-optimized". Bcrypt is such
a hashing facility; unlike hashing algorithms such as MD5 and SHA1, which are
optimized for speed, bcrypt is intentionally structured to be slow.

For sensitive data that must be protected, such as passwords, bcrypt is an
advisable choice.

.. _Flask-Bcrypt: http://github.com/maxcountryman/flask-bcrypt
.. _Flask: http://flask.pocoo.org/

Installation
------------

Install the extension with one of the following commands:

    $ easy_install flask-bcrypt

or alternatively if you have pip installed:
    
    $ pip install flask-bcrypt

Usage
-----

To use the extension simply import the class wrapper and pass the Flask app
object back to here. Do so like this::
    
    from flask import Flask
    from flaskext.bcrypt import Bcrypt
    
    app = Flask(__name__)
    bcrypt = Bcrypt(app)

Two primary hashing methods are now exposed by way of the bcrypt object. Use
them like so::

    pw_hash = bcrypt.generate_password_hash('hunter2')
    bcrypt.check_password_hash(pw_hash, 'hunter2') # returns True

API
___
.. autoclass:: flaskext.bcrypt.Bcrypt
    :members:

.. autofunction:: flaskext.bcrypt.generate_password_hash

.. autofunction:: flaskext.bcrypt.check_password_hash

