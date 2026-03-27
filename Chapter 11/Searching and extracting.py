#search for the lines that starts with 'X' followed by 
# any non whitespace character and ':'
#followed by a space and any number
#the number can include a decimal
import re
file=open('C:/Users/arshia.naeem/Documents/mbox-short.txt')
for line in file:
    #if re.findall('^X\S+: [0-9.]+',line):  
        #print(line)
#then print the number if it is greater than zero
     x=re.findall('^X\S*: ([0-9.]+)',line) # here () in dicates the subset of the data that is selected to be displayed
     if len(x)>0:
        print(x)
#search for lines that start with 'Details: rev='
#followed by numbers
#then print the number if one is found
     b=re.findall('^Details:.*rev=([0-9]+)',line)
     if len(b)>0:
        print(b)
#search for the lines that starts with From and a characeter
#followed by a two digit number between 00 and 99 followed by ':'
#then print the number if one is found
     c=re.findall('^From.*([0-9][0-9]+):', line)
     if len(c)>0:
            print(c)
