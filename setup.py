#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

setup(
    name='anillo',
    version=":versiontools:anillo:",
    description="Ring/compojure like nanoframework build on top of werkzoug",
    long_description="",
    keywords='framework, web, ring, compojure',
    author='Jesús Espino García',
    author_email='jespinog@gmail.com',
    url='https://github.com/jespino/anillo',
    license='BSD',
    packages=['anillo'],
    install_requires=[
        'werkzeug',
    ],
    setup_requires=[
        'versiontools >= 1.9.1',
    ],
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ]
)
