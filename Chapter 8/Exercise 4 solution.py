file=open('C:/Users/arshia.naeem/Documents/romeo.txt')
new=list()
for line in file:
    #print(line)
    line=line.split()
    print(line)
    for i in line:
        if i not in new:
            new.append(i)
new.sort()
print(new)    

#the other way to solve the programm
file=open('C:/Users/arshia.naeem/Documents/romeo.txt')
new=list()
for line in file:
   # print(line) 
   word=line.split()
   #print(word) 
   for i in word:
      #print(i)
      if i not in new:
         new.append(i)
print(new)

    