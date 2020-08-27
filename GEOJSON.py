# In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/geoxml.py. The program will prompt for a URL, read the XML data from that URL using urllib and then parse and extract the comment counts from the XML data, compute the sum of the numbers in the file.
import urllib.request, urllib.parse, urllib.error
import ssl
import json

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
serviceURL = "http://py4e-data.dr-chuck.net/json?"
loc = input('Enter Location - ')
if len(loc) < 1 : loc = "Zagazig University"
url = serviceURL + urllib.parse.urlencode({'address': loc,'key':42})
print(url)
uh = urllib.request.urlopen(url, context=ctx)
inputStream = uh.read().decode()
data = json.loads(inputStream) 
print(data['results'][0]['place_id'])

