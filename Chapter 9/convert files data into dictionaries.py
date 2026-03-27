file=open('c:/Users/arshia.naeem/Documents/words.txt')
d=dict()
new=list()
for line in file:
    #print(line)
    #words=line.split()
    new.append(line)
for i in new:
    words=i.split()
    for w in words:
        if w not in d:
               d[w]=1
        else:
               d[w]=d[w]+1
    #print(i)
#print(new)  
print(d)

####################################################################
file=open('c:/Users/arshia.naeem/Documents/words.txt')
d=dict()
new=list()
for line in file:
    #print(line)
    #words=line.split()
    new.append(line)
for i in new:
        if i not in d:
               d[i]=1
        else:
               d[i]=d[i]+1
    #print(i)
#print(new)  
print(d)