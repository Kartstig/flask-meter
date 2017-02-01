#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'Flask',
]

test_requirements = [
    'pytest'
]

setup(
    name='Flask-Meter',
    version='0.1.2',
    description="Flask-Meter adds a monitoring endpoint for consuming application host metrics.",
    long_description=readme + '\n\n' + history,
    author="Herman Paul Singh",
    author_email='kartstig@gmail.com',
    url='https://github.com/KartStig/flask_meter',
    download_url="https://github.com/KartStig/flask_meter/tarball/0.1.2",
    packages=[
        'flask_meter',
    ],
    package_dir={'flask_meter':
                 'flask_meter'},
    entry_points={
        'console_scripts': [
            'flask_meter=flask_meter.cli:main'
        ]
    },
    include_package_data=True,
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords='flask_meter',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
