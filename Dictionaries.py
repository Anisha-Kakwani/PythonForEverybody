# Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.
name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
dct = dict()
for line in handle:
    if line.startswith("From "):
        words = line.split()
        dct[words[1]]=dct.get(words[1],0) + 1
max=0
qualifier=""
for sender in dct.keys():
    if int(dct[sender]) > max:
        max = dct[sender]
        qualifier = sender  
print(qualifier,":",max)

