import re
count=0
total=0
average=0
try:
    a=input("enter file to open:\n")
except:
    print("YOU HAVE ENTERED AN INVALID FILE NAME:")
    exit()

file=open(a)
for line in file:
    x=re.findall('^New Revision: ([0-9]+)',line)
    count=count+1
    total=total+count
    average=total/count
print(count)
print(total)
print(average)
