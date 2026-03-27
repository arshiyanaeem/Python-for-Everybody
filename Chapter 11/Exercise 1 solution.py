import re
count=0
file=open('c:/Users/arshia.naeem/Documents/mbox-short.txt')
a=input("enter a regular expression")
for line in file:
    if re.findall(f'^{a}',line): #here 'f' makes this a 'formatted string' in this way we have added the input and then gave its count
        count=count+1
print("The",a,"count is:",count)


