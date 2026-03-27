count=0
file = open('C:/Users/arshia.naeem/Documents/mbox.txt')
print(file)
f=file.read()
for line in f:
             if line!='EOF':
                     #print(line) printing this would cause an infinite loop of text file data printing
                     count=count+1
                     #print(f[:20])     
             else:
                 break 
print(count) 
print(f[:20])
print(len(f))

