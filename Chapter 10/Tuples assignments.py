m=['have','fun']
x,y=m #at left side we are having two tuples and in the right side we have list wich is being assighed to left side tuples
print(x,y)
#a,b,c=m # the tuple elements at the left ,must be balanced with the right side assignment
#print(a)
(x,y)
print(x,y)
#to swap two values we use this tuple assignments concept
a=10
b=20
a,b=b,a
print("a is:\n",a)
print("b is\n",b)
#to split a email address into a user name and a domain
addr='monty@python.org'
a=addr.split('@')
print(a)
username=a[0]
domain=a[1]
#or username,domain=a
print(username,"\n",domain)

