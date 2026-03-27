file=open('c:/Users/arshia.naeem/Documents/mbox-short.txt')
d=dict()
for line in file:
    words=line.split()
    if line.startswith('From'):
        e=words[1]
        d[e]= d.get(e,0)+1
print(d)
m=max(d,key=d.get)   
print(m,d[m])
n=min(d,key=d.get)
print(n,d[n])
