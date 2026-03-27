#Retrieving web pages with urllib
import urllib.request

file=urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in file:
    print(line.decode().strip())

