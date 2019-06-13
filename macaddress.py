#!/usr/bin/env python3
import sys
import urllib.request
import json
import codecs
arg1=sys.argv[1]
arg2=sys.argv[2]
url = 'https://api.macaddress.io/v1?apiKey='+arg1+'&output=json&search='+arg2
json_obj = urllib.request.urlopen(url)
reader = codecs.getreader("utf-8")
data = json.load(reader(json_obj))
print ("company Name is " +data['vendorDetails']['companyName']);
print ("comapany Address is " +data['vendorDetails']['companyAddress']);
