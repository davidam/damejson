#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (C) 2019  David Arroyo Menéndez

# Author: David Arroyo Menéndez <davidam@gnu.org>
# Maintainer: David Arroyo Menéndez <davidam@gnu.org>

# This file is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.

# This file is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with damepandas; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor,
# Boston, MA 02110-1301 USA,

import os
import re
import unittest

def my_test_suite():
    test_loader = unittest.TestLoader()
    test_suite = test_loader.discover('tests', pattern='test_*.py')
    return test_suite

from setuptools import setup

# def readme():
#     with open('README.org') as f:
#         return f.read()


setup(name='damejson',
      version='0.0.6',
      description='Learning Json from Tests by David Arroyo Menéndez',
#      long_description=readme(),
      classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3.6',
        'Topic :: Scientific/Engineering',
      ],
      keywords='json tests',
      url='http://github.com/davidam/damejson',
      author='David Arroyo Menéndez',
      author_email='davidam@gnu.org',
      license='GPLv3',
      packages=['damejson', 'damejson.tests', 'damejson.files'],
      package_dir={'damejson': 'damejson', 'damejson.tests': 'damejson/tests', 'damejson.files': 'damejson/files'},
      package_data={'damejson.tests': ['*'],
                    'damejson.files': ['*']},
      data_files=[('damejson', ['damejson/runtests.sh'])],
      install_requires=[
          'markdown',
      ],
      test_suite='setup.my_test_suite',
      include_package_data=True,
      zip_safe=False)
