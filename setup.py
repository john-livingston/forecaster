#!/usr/bin/env python
import os
import sys
import re

try:
    from setuptools import setup
    setup
except ImportError:
    from distutils.core import setup
    setup

if sys.argv[-1] == "publish":
    os.system("python setup.py sdist upload")
    sys.exit()

# Handle encoding
major, minor1, minor2, release, serial = sys.version_info
if major >= 3:
    def rd(filename):
        f = open(filename, encoding="utf-8")
        r = f.read()
        f.close()
        return r
else:
    def rd(filename):
        f = open(filename)
        r = f.read()
        f.close()
        return r

setup(
    name='forecaster',
    packages =['forecaster'],
    version="0.1.1",
    license = ['GNU GPLv3'],
    description ='',
    long_description=rd("README.md") + "\n\n"
                    + "---------\n\n",
    package_dir={"forecaster": "forecaster"},
    package_data={"forecaster": ["data/*.h5"]},
    scripts=[],
    include_package_data=True,
    keywords=[],
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering',
        'Programming Language :: Python'
        ],
    install_requires = ['numpy', 'h5py', 'scipy'],
)
