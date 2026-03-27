#parsing string
#s="banana"
#print(s)
#print(s.find('n',3))
data='From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
a=data.find('@')
b= data. find(' ',a)
result=data[a:b+1]
print(result)
#format operator
one=42
print('The interger is % d string now:\n'% one)
two= 42.5
print('The float is %g string now:\n'% two)
three='String'
print('The string is %s string now:\n'% three)