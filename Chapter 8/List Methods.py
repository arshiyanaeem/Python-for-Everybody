l1=['a','b','c']
#APPEND METHOD
l1.append('z')
print(l1)
while True:
    a=input('enter data to add in the list:\n')
    if a=='done':
        break
    else:
        l1.append(a)
        print(l1)
print("the final list will be:", l1)   

# Extend method (used to compine lists)
l2=['hello','hi','byebye']
l1.extend(l2)
print(l1)

#SORT METHOD (sort data from low to higher)
l1.sort()
print("sorted data is:\n",l1)

#Deleting data in list
#1. when you know the index:
del l1[2]
print(l1)
#2. when you dont know the index
l1.remove('hello')
print(l1)
#3.when you want to delete more than one element
del l1[:3]
print(l1)