l1=[1,2,3,4,5]
print(len(l1))
print(range(len(l1)))
print(sum(l1))
print(min(l1))
print(max(l1))

#take input from the user and create a list place the data in the list then find sum and average of it
new=list() #this will create  list
while True:
     a=input("enter teh number to calculate\n")
     if a=='done':
          break
     b=int(a)
     new.append(b)
     print(new)
     average=sum(new)/len(new)
print(sum)
print(average)



