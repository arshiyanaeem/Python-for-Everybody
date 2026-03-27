file=open('C:/Users/arshia.naeem/Documents/mbox-short.txt')
d=dict()
for line in file:
    words=line.split()
    if line.startswith('From'):
        #59print(words[1])
        e=words[1]
        if e not in d:
            d[e]=1
        else:
            d[e]=d[e]+1
#print(d)    
l=list(d.items())  #converted dictionary into list of tuples
#print(l)
for no,email in l:
   print(no,email) 
l.sort(reverse=True)
print(l)
print(max(l))
print(min(l))