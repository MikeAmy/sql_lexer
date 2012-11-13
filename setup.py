# Copyright (C) 2012 Mike Amy, cocoade@googlemail.com

# Based on a parts of python-sqlparse by Andi Albrecht
# Copyright (C) 2008 Andi Albrecht, albrecht.andi@gmail.com

# This setup script is part of python-sql_lexer and is released under
# the BSD License: http://www.opensource.org/licenses/bsd-license.php.

import os
from distutils.core import setup

import sql_lexer

setup(
    name='sql_lexer',
    version=sql_lexer.__version__,
    packages=find_packages('sql_lexer'),
    description='Simple SQL lexer',
    author='Michael Stephen Amy',
    author_email='cocoade@googlemail.com',
    download_url=DOWNLOAD_URL,
    long_description=LONG_DESCRIPTION,
    license='BSD',
    url='https://github.com/MikeAmy/sql_lexer',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.4',
        'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Topic :: Database',
        'Topic :: Software Development'
    ]
)
