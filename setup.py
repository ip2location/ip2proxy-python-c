#!/usr/bin/env python

from distutils.core import setup

setup(
    name='ip2proxy_python_c',
    version='1.0.0',
    description='IP2Proxy Python library with C module to query an IP address if it was being used as open proxy, web proxy, VPN anonymizer and TOR exits from IP2Proxy database',
    author='IP2Location',
    author_email='support@ip2location.com',
    license='MIT',
    url='https://www.ip2location.com',
	keywords='IP2Proxy, proxies, vpn',
    py_modules=['ip2proxy_python_c'],
)