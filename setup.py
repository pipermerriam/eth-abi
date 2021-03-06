#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import (
    setup,
    find_packages,
)


setup(
    name='eth-abi',
    # *IMPORTANT*: Don't manually change the version here. Use the 'bumpversion' utility.
    version='1.0.0-beta.1',
    description="""Ethereum ABI Utils""",
    long_description_markdown_filename='README.md',
    author='Piper Merriam',
    author_email='pipermerriam@gmail.com',
    url='https://github.com/ethereum/eth-abi',
    include_package_data=True,
    install_requires=[
        'eth-utils>=1.0.0b2,<2.0.0',
    ],
    extras_require={
        'doc': [
            "Sphinx>=1.6.5,<2",
            "sphinx_rtd_theme>=0.1.9",
        ],
    },
    setup_requires=['setuptools-markdown'],
    py_modules=['eth_abi'],
    license="MIT",
    zip_safe=False,
    keywords='ethereum',
    packages=find_packages(exclude=["tests", "tests.*"]),
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
