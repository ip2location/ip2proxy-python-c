# IP2Proxy-Python-C

This library allows user to query an IP address if it was being used as open proxy, web proxy, VPN anonymizer and TOR exits. It lookup the proxy IP address from **IP2Proxy BIN Data** file. This data file can be downloaded at

* Free IP2Proxy BIN Data: https://lite.ip2location.com
* Commercial IP2Proxy BIN Data: https://www.ip2location.com/proxy-database

This library required the **IP2Proxy C Library** to work. You can install it from [here](https://github.com/ip2location/ip2proxy-c).

## Methods

Below are the methods supported in this library.

|Method Name|Description|
|---|---|
|open|Open the IP2Proxy BIN data with the help of **IP2Proxy C Library**.|
|close|Close and clean up the file pointer.|
|get_package_version|Get the package version (1 to 8 for PX1 to PX8 respectively).|
|get_module_version|Get the module version.|
|get_database_version|Get the database version.|
|is_proxy|Check whether if an IP address was a proxy. Returned value:<ul><li>-1 : errors</li><li>0 : not a proxy</li><li>1 : a proxy</li><li>2 : a data center IP address</li></ul>|
|get_all|Return the proxy information in array.|
|get_proxy_type|Return the proxy type. Please visit <a href="https://www.ip2location.com/databases/px4-ip-proxytype-country-region-city-isp" target="_blank">IP2Location</a> for the list of proxy types supported|
|get_country_short|Return the ISO3166-1 country code (2-digits) of the proxy.|
|get_country_long|Return the ISO3166-1 country name of the proxy.|
|get_region|Return the ISO3166-2 region name of the proxy. Please visit <a href="https://www.ip2location.com/free/iso3166-2" target="_blank">ISO3166-2 Subdivision Code</a> for the information of ISO3166-2 supported|
|get_city|Return the city name of the proxy.|
|get_isp|Return the ISP name of the proxy.|
|get_domain|Return the internet domain name associated with IP address range.|
|get_usage_type|Return the usage type classification of ISP or company.|
|get_asn|Return the autonomous system number (ASN).|
|get_as_name|Return the autonomous system (AS) name.|
|get_last_seen|Return the proxy last seen in days.|
|get_threat|Return the threat types reported to proxy's IP address or domain name.|
|get_provider|Returns the VPN service provider name if available.|

## Requirements
1. Python 2.7 and above
2. **[IP2Proxy C Library](https://github.com/ip2location/ip2proxy-c)**

## Installation
1. Unzip the package.
2. Execute `python setup.py build`
3. Execute`python setup.py install`


## Testing
    python sample.py

## Reference

### Usage Type

- (COM) Commercial
- (ORG) Organization
- (GOV) Government
- (MIL) Military
- (EDU) University/College/School
- (LIB) Library
- (CDN) Content Delivery Network
- (ISP) Fixed Line ISP
- (MOB) Mobile ISP
- (DCH) Data Center/Web Hosting/Transit
- (SES) Search Engine Spider
- (RSV) Reserved

## Support
Email: support@ip2location.com.
URL: [https://www.ip2location.com](https://www.ip2location.com)
