#!/usr/bin/env python

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

version = __import__('reloader').__version__

setup(
    name = 'reloader',
    version = version,
    description = 'Dependency-based Python module reloader',
    author = 'Jon Parise @ extended by aukobara@gmail.com',
    author_email = 'jon@indelible.org',
    license = "MIT License",
    url = "https://github.com/aukobara/python-reloader",
    download_url = 'https://github.com/jparise/python-reloader/tarball/' + version,
    classifiers = ['Intended Audience :: Developers',
                   'License :: OSI Approved :: MIT License',
                   'Development Status :: 4 - Beta',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python'],
    py_modules = ['reloader'],
    test_suite = 'tests',
)
