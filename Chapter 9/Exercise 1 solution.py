file=open('C:/Users/arshia.naeem/Documents/words.txt')
d=dict()
for line in file:
    words=line.split()
    for w in words:
        if w not in d:
            d[w]=1
        else:
            d[w]=d[w]+1
l1=list(d.keys())
print(l1)
s=str(input('Enter a string to check:\n'))
if s not in l1:
    print("this string do not exists\n")
else:
    print("this string exists:\n")