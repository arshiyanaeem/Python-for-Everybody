d={'chuck':'1','annie':'42','jan':'200'}
for key in d:
    if d[key]>'10':               
        print(key,d[key])

####the other way
d={'chuck':1,'annie':42,'jan':200}
for k in d:
    if d[k]> 10:
        print(k,d[k])
# print the keys in alphabatical order #### you need to use sort and that is a list function
#1. we need to convert the dictionary into lists
l1=list(d.keys())
#l2=list(d.values())
l1.sort()
for key in l1:
    print(key,d[key])