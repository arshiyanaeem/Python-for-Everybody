#if you wnat to convert a list of strings into numbers to find sum
ls=['40','68','12']
ln=list()
for l in ls:
     ln.append(int(l))
     a=sum(ln)
print(a)