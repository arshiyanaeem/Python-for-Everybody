file=open('c:/Users/arshia.naeem/Documents/mbox-short.txt')
d=dict()
for line in file:
    words=line.split()
    #print(words)
    if line.startswith('From') and len(words)>2:
        #print(line)
        e=words[5]
        #print(e)
        a=e.split(':')
        #print(a)
        if a[0] not in d:
            d[a[0]]=1
        else:
            d[a[0]]=d[a[0]]+1
#print(d)
l=list(d.items())
#print(l)
for hour,times in l:
    print(hour,times,'\n')
