# program that counts the number of times the letter 'a' appears in a string
count=0
fruit='banana'
index=0
while index< len(fruit):
            if fruit[index]=='a':
                    count=count+1
            index=index+1
print("total number of 'a' is:\n",count)