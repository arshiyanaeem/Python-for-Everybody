#dictionaries used to count the words in a string
s='hellohibyebyehowislifegoingon'
count=dict()
for line in s:
    word=line.split()
    print(word)
    for w in word:
        if w not in count:
            count[w]=1
        else:
            count[w]=count[w]+1
print(count)