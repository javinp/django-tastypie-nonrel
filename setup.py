#!/usr/bin/env python
# -*- coding: utf-8 -*-
from distutils.core import setup

CLASSIFIERS = [
    'Intended Audience :: Developers',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
]

setup(
    name='django-tastypie-nonrel',
    version='0.0.2',
    description='Nonrelational extensions for Django Tastypie.',
    author='Andres Douglas',
    author_email='andres.douglas@gmail.com',
    url='https://github.com/andresdouglas/django-tastypie-nonrel',
    packages=[
        'tastypie_nonrel',
    ],
    requires=[
        'tastypie',
    ],
)
