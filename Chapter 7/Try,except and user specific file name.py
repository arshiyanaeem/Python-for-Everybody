file=input('Enter complet file name with its path')
try:
   f=open(file)
   #f=f.read() If i will use this it will not open the file 
#file=open('C:/Users/arshia.naeem/Documents/mbox-short.txt')
except:
   print('illegal file name this file did not found.')
   #exit()
for line in f:
   if line.startswith('From:'):
      print(line)
  


