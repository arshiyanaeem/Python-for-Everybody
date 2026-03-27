s={'one':'100','two':'20','three':'30','four':'4','five':'50','six':'30060'}
a=s.get('five',0)
print(a)
b=s.get('hello',90)
print(b)

#couunt each character in string usinf dictionary
s='hellohibyebyewhttodonowwheniseeyouhow'
d=dict()
for i in s:
    d[i]=d.get(i,0)+1
    #print(d[i])
print(d)
        