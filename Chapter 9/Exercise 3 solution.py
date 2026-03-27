file=open('C:/Users/arshia.naeem/Documents/mbox-short.txt')
d=dict()
for line in file:
    words=line.split()
    if line.startswith('From'):
        #print( words[1])
        if words[1] not in d:
            d[words[1]]=1
        else:
            d[words[1]]=d[words[1]]+1
print(d)


    