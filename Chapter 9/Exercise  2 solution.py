file=open('C:/Users/arshia.naeem/Documents/mbox.txt')
d=dict()
for line in file:
                 words=line.split()
                 #print(words)
                 if line.startswith('From') and len(words)>3:
                         print(words[2])
                         if words[2] not in d:
                                 d[words[2]]=1
                         else:
                                 d[words[2]]=d[words[2]]+1
print(d)
