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
# to find maximum by converting dictionaries into lists but this will give maximum on the basis of key and its a bit inaccurate
l1=list(d.keys())
l2=list(d.keys())
a=max(l1)
b=min(l2)
print("maximum value:\n",a,d[a])
print("minimum value:\n",b,d[b])