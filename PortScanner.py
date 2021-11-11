import os
import sys

## Provide an Ip Address in the arguments call .. and that's it
# This Tool Scans For Http Servers with specific ip 
##### basic usage #####
# python3 PortScanner.py <victim Ip>
ip_address = sys.argv[1]
for i in range(65000):
  result = os.system("curl %s:%d 2>/dev/null | grep -w '<html>'" %(ip_address ,i))
  if ( result == 0 ):
    print(str(ip_address) + ":" + str(i))
