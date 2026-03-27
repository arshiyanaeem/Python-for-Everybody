
def count(x,y):
 c=0
 index=0
 while index< len(x):
            if x[index]==y:
                    c=int(c+1)
            index=int(index+1)
 return c


fruit='banana'
letter='a'
f=str(fruit)
l=str(letter)
z=count(f,l)
print("total number of 'a' is:\n",int(z), "\nThe fruit namne is:\n",fruit)