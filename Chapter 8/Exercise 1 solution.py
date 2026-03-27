def chop(x):
     a=int(len(x))
     del x[a-1]
     del x[0]
     #print(x)
     middle(x) #function calling the other function

def middle(y):
        #print(y)
        return y
     
           
l=[1,2,3,4,5,6]
chop(l)
print(l)

