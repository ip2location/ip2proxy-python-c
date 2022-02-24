#!/usr/bin/env python

# from distutils.core import setup
import setuptools

with open("README.md", "r") as fh:
	long_description = fh.read()

setuptools.setup(
	name="ip2proxy_python_c",
	version="2.1.0", 
	author="IP2Location",
	author_email="support@ip2location.com",
	description="IP2Proxy Python library with C module to query an IP address if it was being used as open proxy, web proxy, VPN anonymizer and TOR exits from IP2Proxy database",
	long_description=long_description,
	long_description_content_type="text/markdown",
	py_modules=['ip2proxy_python_c'],
	url="https://github.com/ip2location/ip2proxy-python",
	packages=setuptools.find_packages(),
	classifiers=[
		"Development Status :: 5 - Production/Stable",
		"Intended Audience :: Developers",
		"Topic :: Software Development :: Libraries :: Python Modules",
		"Programming Language :: Python :: 3",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
	],
)