def computerpay(h,r):
                    c=(int(h)*float(r))+25
                    return c

a=int(input('enter hours:\n'))
b= float(input('enter rate:\n'))
x=computerpay(a,b)
print("the pay is:\n",float(x))
