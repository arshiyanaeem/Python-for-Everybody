file=input("enter file to read or open:\n")
try:
    if file=='NA NA BOO BOO':
        print("NA NA BOO BOO, you too ;)")
    else:    
       f=open(file)
except:
        print("This file did not exists")