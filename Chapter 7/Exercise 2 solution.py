count=0
total=0
average=0
file=input('enter the complet path of a file:\n')
f=open(file)
for line in f:
    if line.find('X-DSPAM-Confidence')!=-1:
        count=count+1
        total=count+total
        average=total/count 
        print(line)      
print(count)
print(total)
print(average)


