'''
    Flask-Bcrypt
    ------------
    
    Bcrypt hashing for your Flask.
'''

from setuptools import setup

setup(
    name='Flask-Bcrypt',
    version='0.5.2',
    url='https://github.com/maxcountryman/flask-bcrypt',
    license='BSD',
    author='Max Countryman',
    author_email='maxc@me.com',
    description='Brcrypt hashing for Flask.',
    long_description=__doc__,
    py_modules=['flask_bcrypt'],
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
    ],
    test_suite='test_bcrypt'
)

