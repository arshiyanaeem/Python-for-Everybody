import string
f=input('enter the file to open')
try:
    file=open(f)
except:
    print("ther file is not available\n")  
    exit() 
d=dict()

#file=open('C:/Users/arshia.naeem/Documents/romeo.txt')
for line in file:
    line=line.rstrip()
    line=line.translate(str.maketrans('','',string.punctuation)) # this is used to make who,WHO problems resolve remove punctuations##its format is :line.translate(str.maketrans('fromstr','tostr','deletestr)
    line=line.lower()
    words=line.split()
    for w in words:
       # w=w.translate(str.maketrans('','',string.punctuation)) # this is used to make who,WHO problems resolve remove punctuations##its format is :line.translate(str.maketrans('fromstr','tostr','deletestr)
        if w not in d:
            d[w]=1
        else:
            d[w]=d[w]+1
print(d)