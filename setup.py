# -*- coding: utf-8 -*-
import os
import sys
import re

from setuptools import setup

dependencies = [
    'opencv-python'
]


setup(
    name="face_recognition",
    version='0.1',
    package_data={'pymlconf': ['tests/conf/*', 'tests/files/*']},
    install_requires=dependencies,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: MIT License",
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries'
    ],
    test_suite='face_recognition.tests',
)
