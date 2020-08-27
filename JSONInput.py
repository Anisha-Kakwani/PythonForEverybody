# In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/geoxml.py. The program will prompt for a URL, read the XML data from that URL using urllib and then parse and extract the comment counts from the XML data, compute the sum of the numbers in the file.
from urllib.request import urlopen
import ssl
import json

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
url = input('Enter - ')
if len(url) < 1 : url = "http://py4e-data.dr-chuck.net/comments_737938.json"
inputStream = urlopen(url, context=ctx).read()
data = json.loads(inputStream) 
comments = data['comments']
sum = 0
for item in comments:
    sum += int(item['count'])
print(sum)

