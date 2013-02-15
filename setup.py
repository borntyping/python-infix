#!/usr/bin/env python

from setuptools import setup

setup(
    name             = 'infix',
    version          = '0.1',
    license          = 'MIT License',
    url              = 'https://github.com/borntyping/infix',

    author           = 'Sam Clements',
    author_email     = 'sam@borntyping.co.uk',

    description      = 'Infix operators for Python',
    long_description = open('README.rst').read(),

    py_modules       = ['infix'],

    classifiers      = [
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Libraries',
        'Topic :: Utilities',
    ],
)
