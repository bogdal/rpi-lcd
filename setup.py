# -*- coding: utf-8 -*-
from setuptools import setup, find_packages


setup(
    name='rpi-lcd',
    version='0.0.3',
    description='I²C LCD library for RaspberryPi',
    author='Adam Bogdał',
    author_email='adam@bogdal.pl',
    url='https://github.com/bogdal/rpi-lcd',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'smbus'],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: System :: Hardware :: Hardware Drivers'],
    zip_safe=False)
