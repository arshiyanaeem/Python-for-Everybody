#Program to retrieve an image across using HTTP.
#instead of copying the data to the screen as the program runs, we accumulate the data in a string
#trim off the headers, and then save the image data to a file :
import socket
import time

HOST = 'data.pr4e.org'
PORT = 80
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect((HOST, PORT))
mysock.sendall(b'GET http://data.pr4e.org/cover3.jpg HTTP/1.0\r\n\r\n')

count = 0
picture = b""

while True:
    data = mysock.recv(5120)
    if len(data) < 1:
        break
    # Accumulate all data chunks into the 'picture' variable
    count = count + len(data)
    print(len(data), count)
    picture = picture + data

# Close the socket ONLY after the loop is done
mysock.close()

# Look for the end of the header (double carriage return/line feed)
pos = picture.find(b"\r\n\r\n")
print('Header length', pos)
print(picture[:pos].decode())

# Skip past the header (pos + 4 bytes) and save the binary data
picture = picture[pos+4:]
fhand = open("c:/Users/arshia.naeem/Documents/stuff.jpg", "wb")
fhand.write(picture)
fhand.close()

print("\nImage saved to stuff.jpg")