def computegrade(g):
                   if g >=0.9:
                             return ('A')
                   elif (g>=0.8):
                             return ('B')
                   elif (g>=0.7):
                           return ('C')
                   elif (g>=0.6):
                           return ('D')
                   else:
                        return ('F')    



a= float(input("enter score between range 0.0-1.0:\n"))
b=computegrade(a)
print("Grade is:\n",str(b))