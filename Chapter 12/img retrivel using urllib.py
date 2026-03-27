#reading binary files using urllib to raed any size of data without halting memory
import urllib.request, urllib.parse, urllib.error

img_handle = urllib.request.urlopen('http://data.pr4e.org/cover3.jpg')
file = open('C:/Users/arshia.naeem/Documents/cover.jpg', 'wb')

size = 0
while True:
    # Read only 100,000 bytes at a time from the handle
    info = img_handle.read(100000)
    if len(info) < 1:
        break
    
    size = size + len(info)
    file.write(info)

print(size, 'characters copied!')

file.close()
img_handle.close() # Good practice to close the web handle too