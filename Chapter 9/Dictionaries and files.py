file=open('c:/Users/arshia.naeem/Documents/romeo.txt')
d=dict()
for line in file:
    words=line.split()
    for w in words:
        #print(w)
        if w not in d:
            d[w]=1
        else:
            d[w]=d[w]+1
print(d)
#to print each key and its corresponding values using loop
#i=0
d={'chuck':'1','annie':'42','jan':'200'}
for key in d:
    print(key,d[key]) # this will print key with its corresponding values
    print(d[key]) # this is used to print values
    print(key) #this is used to print keys
    #print(key[i])
   # i=i+1
    if d[key]>'10':               ##to filter the valus in dictionaries above 10##########
        print(key,d[key])
