a=dict()
#print(a)
while True:
    b=input("Enter key dictionaries:\n")
    c=input("Enter values against each key:\n")
    a[b]=c
    if b =='done' and c == 'done':
        break  
print(a)    
print(len(a))
if 'one' in a:
       print("the key exists:\n")
else:
     print("this key do not exists\n")
#to check value in dictionaries we will convert the values into list then check
value= list(dict.values(a))
if '1' in value:
          print("value exists")
else:
    print("this value not exists\n")
#convert the values and keys into lists:
a={'one':'1','two':'2','three':'3','four':'4','five':'5'} #a format to write dictionaries {'KEY':'VALUE'}
b=list(a.values())
print(b)
c=list(a.keys())
print(c)
d=list(dict.values(a))
print(d)
e=list(dict.keys(a))
print(e)
# append the dictionaries items keys and values
a={'one':'1','two':'2','three':'3','four':'4','five':'5'}
print(a.keys())
print(a.values())
l1=list(a.keys())
l2=list(a.values())
l1.append(l2)
print(l1)