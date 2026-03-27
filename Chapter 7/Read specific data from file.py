file=open('C:/Users/arshia.naeem/Documents/mbox-short.txt')
#f=file.read() this is restrired to read data as per memorylimitation
for line in file:
           #line.strip()
           #if line.startswith('From'): #to print all txt file data finish this if condition
            #print(line)
            if not line.startswith('From'):
                  continue
            print(line)
            #if line.find('zqian@umich.edu') == -1:
                    #break
            #print("done for now!")
