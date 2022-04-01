import os

from setuptools import setup

this_directory = os.path.dirname(__file__)
module_path = os.path.join(this_directory, 'flask_bcrypt.py')
version_line = [line for line in open(module_path)
                if line.startswith('__version_info__')][0]
with open(os.path.join(this_directory, 'README.markdown')) as f:
    long_description = f.read()

__version__ = '.'.join(eval(version_line.split('__version_info__ = ')[-1]))

setup(
    name='Flask-Bcrypt',
    version=__version__,
    url='https://github.com/maxcountryman/flask-bcrypt',
    license='BSD',
    author='Max Countryman',
    author_email='maxc@me.com',
    description='Brcrypt hashing for Flask.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    py_modules=['flask_bcrypt'],
    zip_safe=False,
    platforms='any',
    install_requires=['Flask', 'bcrypt>=3.1.1'],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    test_suite='test_bcrypt'
)
