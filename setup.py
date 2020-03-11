#!/usr/bin/env python
# -*- coding: utf-8 -*-
from distutils.core import setup

with open('README.md', 'r') as fh:
  LONG_DESCRIPTION = fh.read()

DESCRIPTION = 'A Twitter SDK to help API consume.'
URL = 'https://github.com/user/jessescn'
DOWNLOAD_URL = 'https://github.com/jessescn/TwitterSDK/archive/0.1.tar.gz'

VERSION = '0.0.1'

CLASSIFIERS = [
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
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
  long_description_content_type='text/markdown',
  author='Jessé Souza',
  author_email='jesse.neto@ccc.ufcg.edu.br',
  url=URL,
  download_url=DOWNLOAD_URL,
  keywords=['Twitter', 'API','Python', 'SDK'],
  install_requires=['requests'],
  classifiers=CLASSIFIERS
)