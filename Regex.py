# The basic outline of this problem is to read the file, look for integers using the re.findall(), looking for a regular expression of '[0-9]+' and then converting the extracted strings to integers and summing up the integers.
import re

name = input("Enter file:")
if len(name) < 1 : name = "regex.txt"
handle = open(name)
numList = list()
for line in handle:
    numbers = []
    numbers = re.findall('[0-9]+',line)
    numList = numList + numbers
sum = 0
for item in numList:
    sum = sum + int(item)
print(sum)



