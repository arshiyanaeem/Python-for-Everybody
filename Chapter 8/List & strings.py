# we can make a string as list (it convert each charater of string as single list element)
s='hello'
t=list(s)
print(t)
#split method(it is used to convert the words of strings in words of list)
s='hello hi byebye what to do now?'
t=s.split()
a=list(t)
print(a)
# split using argument
s='split-split-split-split'
delimiter= '-'
b=s.split(delimiter)
print(list(b))
#join method to make list again string
s='this-was-the-string-first-and-now-its-list'
delimiter='-'
t=s.split(delimiter)
print("list is:\n",list(t))
#back to string from list
delimiter='-'
n=delimiter.join(t)
print(n)
#write a program that looks for lines where line starts with "FROM", split those lines and then print the third word in the line
file=open('C://Users/arshia.naeem/Documents/mbox-short.txt')
for line in file:
    #line=line.rstrip()
    if not line.startswith('From'): 
        continue
    word=line.split()
    #print(word)
    if len(word)== 2:
        continue
    print(word[2])
# ANOTHER WAY TO SOLVE THIS PROGRAMM
file=open('C://Users/arshia.naeem/Documents/mbox-short.txt')
for line in file:
    word=line.split()
    if line.startswith('From') and len(word)>=3:
                 print(word[2])
    else:
          continue
