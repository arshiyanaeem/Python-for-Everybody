new=list()
while True:
    a=input("Enter the lists elements:\n",)
    if a=='done':
        break
    new.append(a)
    print()
print(max(new))
print(min(new))