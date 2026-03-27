import re
file=open('c:/Users/arshia.naeem/Documents/mbox-short.txt')
for line in file:
    if re.search('From:',line):
        print(line)
#select the line that starts with some 'xyz' we use symbol:^
    if re.search('^Received',line):
           print(line)
#serach for line that sarts with 'F' follwoed by two characters,followed by 'm:'
    if re.search('^F..m:',line):
                 print(line)
#search for line that starts with 'F' and have an '@' sign
    if re.search('^F.+@',line): # we will use wild card [.+]
           print(line) 

