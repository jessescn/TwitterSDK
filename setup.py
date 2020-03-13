#!/usr/bin/env python
# -*- coding: utf-8 -*-
from distutils.core import setup

DESCRIPTION = 'A Twitter SDK to help API consume.'
URL = 'https://github.com/user/jessescn'
DOWNLOAD_URL = 'https://github.com/jessescn/TwitterSDK/archive/0.0.4.zip'

LONG_DESCRIPTION = "With this SDK you can consume the twitter API in a abstract and encapsulated way. Twitter Developer account is all you need to start creating your applications consuming this Twitter SDK."

VERSION = '0.0.4'

CLASSIFIERS = [
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
]

setup(
  name='TwitterSDK',   
  packages=['TwitterSDK'],
  version=VERSION,
  license='MIT',
  description=DESCRIPTION,
  long_description=LONG_DESCRIPTION,
  author='Jessé Souza',
  author_email='jesse.neto@ccc.ufcg.edu.br',
  url=URL,
  download_url=DOWNLOAD_URL,
  keywords=['Twitter', 'API','Python', 'SDK'],
  install_requires=['requests'],
  classifiers=CLASSIFIERS
)