d={'a':10,'b':1,'c':22}
print(d.items()) # the item return output as tuples for dictionaries with key-value format of dictionaries in tuples
#converting dictionary to a list of tuples and output the contents of a dictionary sorted by the key
l=list(d.items()) #makes list of tuples 
#print(l)
l.sort()
print(l)
# keys and values of dictionaries in a single loop
a={'one':1,'two':2,'three':3}
t=list()
for key,val in list(a.items()):
    #print(key,val)
    print(val,key)
    t.append((key,val))
print(t)
t.sort(reverse=True)
print(t)

