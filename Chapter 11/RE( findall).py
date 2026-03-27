#we want to pull the email addressfrom each of the lines
import re
file=open('c:/Users/arshia.naeem/Documents/mbox-short.txt')
for line in file:
         line=line.rstrip()
         x= re.findall('[A-Za-z0-9]\S*@\S*[a-z]',line)
         if len(x)>0:
            print(x)
#Search for lines that have an at sign between characters 
# the characters must be a letter or number
         a=re.findall('[A-Za-z0-9]\S*@\S[a-z]',line)
         if len(a)>0:
                  print('########################')
                  print(line)
#only to print email addresses from the string input
s='A message from csev@umich.edu to cwen@iupui.edu about meeiting @2PM'
a=re.findall('\S+@\S+',s)
print(a)

        