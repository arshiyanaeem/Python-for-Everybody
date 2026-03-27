#you have a listof words and you want to sort them from longest to shortest
l=['one','two','three','four','five']
l.sort(reverse=True) # smallet to largest order
print(l)
l.sort() # largest to smaller order
print(l)
l=[100,3,555,9999,0,1]
l.sort()
print(l)
#sort the string from longets to shortest
s='but soft what light in younder window breaks'
l=s.split()
t=list()
for w in l:
    t.append((len(w),w)) 
    #t.append(w)
    #print (t)
t.sort(reverse=True)
print(t)
#another way to sort
s='but soft what light in younder window breaks'
l=s.split()
t=list()
t=t+l
t.sort(reverse=True)
print(t)