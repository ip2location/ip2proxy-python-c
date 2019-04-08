from ctypes import *
from ctypes.util import find_library

_VERSION = '1.0.0'
_INVALID_IP_ADDRESS  = 'INVALID IP ADDRESS'

class C_IP2ProxyRecord(Structure):
    '''
        Define the IP2Location Record result structure.
    '''
    _fields_=[("country_short",c_char_p),("country_long",c_char_p),("region",c_char_p),("city",c_char_p),("isp",c_char_p),("is_proxy",c_char_p),("proxy_type",c_char_p)]

class IP2Proxy(object):
    def __init__(self, filename=None, libraryname = None):
        ''' Creates a database object and opens a file if filename is given '''
        if filename:
            self.open(filename)
        if libraryname:
            self.load(libraryname)
        else:
            self.ip2proxy_c = CDLL(find_library('IP2Proxy'))

    def load(self, libraryname):
        '''
            Function to load the IP2Location C Library if user choose to load their own copy of IP2Location C Library.
        '''
        self.ip2proxy_c = CDLL(libraryname)

    def open(self, filename):
        ''' Opens a database file '''
        self.ip2proxy_c.IP2Proxy_open.argtypes = [c_char_p]
        self.ip2proxy_c.IP2Proxy_open.restype = c_void_p
        self.ip2proxy_c_pointer = self.ip2proxy_c.IP2Proxy_open(filename)

    def get_module_version(self):
        return _VERSION

    def get_package_version(self) :
        self.ip2proxy_c.IP2Proxy_get_package_version.argtypes = [c_void_p]
        self.ip2proxy_c.IP2Proxy_get_package_version.restype = c_char_p
        ip2proxy_package_version = self.ip2proxy_c.IP2Proxy_get_package_version(self.ip2proxy_c_pointer)
        return str(ip2proxy_package_version)

    def get_database_version(self) :
        self.ip2proxy_c.IP2Proxy_get_database_version.argtypes = [c_void_p]
        self.ip2proxy_c.IP2Proxy_get_database_version.restype = c_char_p
        ip2proxy_database_version = self.ip2proxy_c.IP2Proxy_get_database_version(self.ip2proxy_c_pointer)
        return str(ip2proxy_database_version)

    def get_all(self, ip):
        ''' Get the whole record with all fields read from the file '''
        ''' set the argument and response types of the function for data compatibility issue. '''
        self.ip2proxy_c.IP2Proxy_get_all.argtypes = [c_void_p, c_char_p]
        self.ip2proxy_c.IP2Proxy_get_all.restype = POINTER(C_IP2ProxyRecord)
        try:
            self.rec = self.ip2proxy_c.IP2Proxy_get_all(self.ip2proxy_c_pointer, ip)
            country_short = self.rec.contents.country_short
            country_long = self.rec.contents.country_long
            region = self.rec.contents.region
            city = self.rec.contents.city
            isp = self.rec.contents.isp
            proxy_type = self.rec.contents.proxy_type
            is_proxy = self.rec.contents.is_proxy
        except:
            country_short = _INVALID_IP_ADDRESS
            country_long = _INVALID_IP_ADDRESS
            region = _INVALID_IP_ADDRESS
            city = _INVALID_IP_ADDRESS
            isp = _INVALID_IP_ADDRESS
            proxy_type = _INVALID_IP_ADDRESS
            is_proxy = -1
        results = {}
        results['is_proxy'] = is_proxy
        results['proxy_type'] = proxy_type
        results['country_short'] = country_short
        results['country_long'] = country_long
        results['region'] = region
        results['city'] = city
        results['isp'] = isp
        return results

    def get_country_short(self, ip):
        ''' Get country_short '''
        try:
            record = self.get_all(ip)
            country_short = record['country_short']
        except:
            country_short = _INVALID_IP_ADDRESS
        return country_short

    def get_country_long(self, ip):
        ''' Get country_long '''
        try:
            record = self.get_all(ip)
            country_long = record['country_long']
        except:
            country_long = _INVALID_IP_ADDRESS
        return country_long

    def get_region(self, ip):
        ''' Get region '''
        try:
            record = self.get_all(ip)
            region = record['region']
        except:
            region = _INVALID_IP_ADDRESS
        return region

    def get_city(self, ip):
        ''' Get city '''
        try:
            record = self.get_all(ip)
            city = record['city']
        except:
            city = _INVALID_IP_ADDRESS
        return city

    def get_isp(self, ip):
        ''' Get isp '''
        try:
            record = self.get_all(ip)
            isp = record['isp']
        except:
            isp = _INVALID_IP_ADDRESS
        return isp

    def get_proxy_type(self, ip):
        ''' Get usage_type '''
        try:
            record = self.get_all(ip)
            proxy_type = record['proxy_type']
        except:
            proxy_type = _INVALID_IP_ADDRESS
        return proxy_type

    def is_proxy(self, ip):
        ''' Determine whether is a proxy '''
        try:
            record = self.get_all(ip)
            is_proxy = record['is_proxy']
        except:
            is_proxy = -1
        return is_proxy

    def close(self):
        self.ip2proxy_c.IP2Proxy_close.argtypes = [c_void_p]
        self.ip2proxy_c.IP2Proxy_close(self.ip2proxy_c_pointer)