#reading binary files using urllib
import urllib.request,urllib.parse,urllib.error

img=urllib.request.urlopen('http://data.pr4e.org/cover3.jpg').read()
file=open('C:/Users/arshia.naeem/Documents/cover3.jpg','wb')
file.close()
print("image sucessfully read\n")