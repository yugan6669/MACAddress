#!/usr/bin/env python3
import sys
import urllib.request
import json
import codecs
def getData():
  try:
    API_KEY=sys.argv[1]
    MAC_ADDRESS=sys.argv[2]
    url = 'https://api.macaddress.io/v1?apiKey='+API_KEY+'&output=json&search='+MAC_ADDRESS
    json_obj = urllib.request.urlopen(url)
    reader = codecs.getreader("utf-8")
    data = json.load(reader(json_obj))
  except IndexError:
    print("Please enter API_KEY and MAC_ADDRESS as arguments")
  except Exception:
    print("Please enter valid API KEY and MAC Address")
  else:
    print("company Name  for MAC Address: "+data['macAddressDetails']['searchTerm'] + " is  "+data['vendorDetails']['companyName']);
    print("Company Address is " +data['vendorDetails']['companyAddress']);
if __name__ == "__main__":
    getData()


