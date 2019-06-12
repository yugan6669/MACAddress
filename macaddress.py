import urllib.request
import json
import codecs
url = 'https://api.macaddress.io/v1?apiKey=at_Jkpyix2qvXMRA29casQxJ1nqioU8b&output=json&search=44:38:39:ff:ef:57'
json_obj = urllib.request.urlopen(url)
reader = codecs.getreader("utf-8")
data = json.load(reader(json_obj))
#print (data)
print ("company Name is " +data['vendorDetails']['companyName']);
print ("comapany Address is " +data['vendorDetails']['companyAddress']);
