t1=('a',)
print(type(t1))
t1=('a')
print(type(t1))
t2=tuple()
print(t2)
t2=tuple([1,2,3])
print(t2)
t2=tuple('string')
print(t2)
t3=(1,2,3,4,5,6,)
print(t3[3])
#slicing
print(t3[2:4])
#tuple can not be modified
t=('A',)+t3[2:]
print(t)