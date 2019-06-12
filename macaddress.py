import urllib.request
import json
import codecs
url = ''
json_obj = urllib.request.urlopen(url)

reader = codecs.getreader("utf-8")

data = json.load(reader(json_obj))

#print (data)

print ("company Name is " +data['vendorDetails']['companyName']);

print ("comapany Address is " +data['vendorDetails']['companyAddress']);
