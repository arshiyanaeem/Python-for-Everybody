sum=0
count=0
average=0
b=0
c=0
while True:
 try:
    line=input("enter number:\n")
    if line=='done':
        print("maximum value is:",b)  
        print("sum is:\n",sum)
        print("count is\n",count)
        print("average is:\n",average)
        print("minimum is:\n",c)
        break
    a=int(line)
    count=count+1
    sum=sum+a
    average=sum/count
    if a>b:
        b=a
    if c==0:
       c=a
    if c>a:
        c=a
 except:
    print("INVALID ENTER AGAIN:\n")
    continue
print("DONE!")

  