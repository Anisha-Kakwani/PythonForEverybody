# In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/geoxml.py. The program will prompt for a URL, read the XML data from that URL using urllib and then parse and extract the comment counts from the XML data, compute the sum of the numbers in the file.
import xml.etree.ElementTree as ET
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
url = input('Enter - ')
if len(url) < 1 : url = "http://py4e-data.dr-chuck.net/comments_737937.xml"
xml = urlopen(url, context=ctx).read()
tree = ET.fromstring(xml)
comments = tree.findall('comments')
comment = comments[0].findall('comment')
sum = 0
for item in comment:
    sum += int(item.find('count').text)
print(sum)

