def delete(x):
    del x[0]

l=[1,2,3,4,5]
delete(l)
print(l)

t1=[1,2]
t2=t1.append('a')
print(t1)
print(t2)

t3=t1+[3]
print(t3)
print(t1)

def data(x):
   return x[3:]

l=['hello','hi','byebye',1,2,3,4,5]
a=data(l)
print(l)
print(a)