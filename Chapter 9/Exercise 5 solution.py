file=open('C:/Users/arshia.naeem/Documents/mbox-short.txt')
d=dict()
for line in file:
    words=line.split()
    if line.startswith('From') and line.find('@') and len(words)>3:
               #print(words[1])
               e=words[1]
               a=e.split('@')
               #print(a)
               print(a[1])
               b=a[1]
               if b not in d:
                       d[b]=1
               else:
                    d[b]=d[b]+1
print(d)
                       