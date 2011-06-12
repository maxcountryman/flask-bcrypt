'''
Flask-Bcrypt
------------

Flask-Bcrypt provides bcrypt support for use with hashing passwords. Two 
functions can be used together to hash passwords `generate_password_hash` and 
then check passwords against a hash `check_password_hash`.

This extension requires py-bcrypt.
'''
from setuptools import setup


setup(
    name='Flask-Bcrypt',
    version='0.1',
    url='https://github.com/maxcountryman/flask-bcrypt',
    license='BSD',
    author='Max Countryman',
    author_email='maxc@me.com',
    description='Bcrypt support for hashing passwords',
    long_description=__doc__,
    packages=['flaskext'],
    namespace_packages=['flaskext'],
    zip_safe=False,
    platforms='any',
    install_requires=[
        'Flask',
        'py-bcrypt'
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)

