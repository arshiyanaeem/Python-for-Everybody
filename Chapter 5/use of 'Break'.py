count=0
sum=0
average=0
while True:
    try:   
        line=input("enter value\n")
        if line=='done' or line=='/':
                print("sum is\n",sum)
                print("the count is\n",count)
                print("the average\n",average)
                break
        count=count+1
        a=float(line)
        sum=sum+a
        average=sum/count
    except:
         print("INVALID INPUT ONLY NUMBERS ARE ALLOWED ENTER AGAIN!")
    continue     
print("DONE!")