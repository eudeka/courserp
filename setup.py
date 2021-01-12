# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in courserp/__init__.py
from courserp import __version__ as version

setup(
	name='courserp',
	version=version,
	description='Course for Eudeka',
	author='eudeka.id',
	author_email='ibnu@eudeka.id',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
