#!/usr/bin/env python

from setuptools import setup

setup(
    name             = 'infix',
    version          = '1.2',
    license          = 'MIT License',
    url              = 'https://github.com/borntyping/python-infix',

    author           = 'Sam Clements',
    author_email     = 'sam@borntyping.co.uk',

    description      = 'Infix operators for Python',
    long_description = open('README.rst').read(),

    py_modules       = ['infix'],

    classifiers      = [
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Software Development :: Libraries',
        'Topic :: Utilities',
    ],
)
