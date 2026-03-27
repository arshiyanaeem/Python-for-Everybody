try:
    a=int(input('enter hours:\n'))
    b=float(input('enter rate:\n'))

    if a > 40:
              pay=((((a)*1.5)*b)+25)
              print('more pay is:', float(pay))
    else:
        pay= (((a)*(b))+25)
        print('pay is:',float(pay))

except:
       print('invalid values try again:')


 


