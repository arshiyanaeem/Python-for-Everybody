count=0
file=open('C:/Users/arshia.naeem/Documents/mbox.txt')
for line in file:
    if line.startswith('From'):
        words=line.split()
        print(words[1])
        count=count+1
print("Total :From: are:\n",count)

