#!/usr/bin/env python3
import sys
import urllib.request
import json
import codecs
API_KEY=sys.argv[1]  
MAC_ADDRESS=sys.argv[2] 
url = 'https://api.macaddress.io/v1?apiKey='+API_KEY+'&output=json&search='+MAC_ADDRESS
json_obj = urllib.request.urlopen(url)
reader = codecs.getreader("utf-8")
data = json.load(reader(json_obj))
print ("company Name is "+data['vendorDetails']['companyName']+ 'MAC Address is'+MAC_ADDRESS  );
