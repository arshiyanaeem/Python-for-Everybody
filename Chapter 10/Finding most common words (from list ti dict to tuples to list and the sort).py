#To print the ten most common words in the text file romeo.txt
#1.create list to dictionary
file=open('C:/Users/arshia.naeem/Documents/romeo.txt')
d=dict()
for line in file:
    words=line.split()
    for w in words:
        if w not in d:
            d[w]=1
        else:
            d[w]=d[w]+1
print(d)
#2.Now dictionary to list of tuples
l=list(d.items())
print(l)
# sort the dictionary by value
l2=list()
for key,val in l:
     l2.append((val,key))
#print(l2)
l2.sort(reverse=True)
for key,val in l2[:10]:
    print(key,val)