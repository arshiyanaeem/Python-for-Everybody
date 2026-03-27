import string
file=open('c:/Users/arshia.naeem/Documents/letter_frequency.txt')
d=dict()
t=list()
for line in file:
    if line.startswith('Letter'):continue
    a=line.translate(str.maketrans('', '', string.punctuation))
    b=a.lower()
    #print(b)
    t.append((b[1],b[0]))
#print(t)
t.sort()
print(t)