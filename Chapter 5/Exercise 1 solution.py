n=4
b=0
while n!=0:
    line=input("enter number:\n")
    if line=='done':
        break
    a=int(line)
    if a>b:
        b=a
    n=n-1
print("maximum value is:",b)    