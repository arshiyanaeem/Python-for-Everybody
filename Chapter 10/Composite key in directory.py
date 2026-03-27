# A telephone directory that maps from lastname, firstname, and number  use concept of composite key (last,first)
directory={('arshia','naeem'):'050110',('rimsha','naeem'):'52247',('komal','naeem'):'41275'}
#(last,first)=directory
l=list(directory.items())
#print(l)
for (la,f),n in l:
    print(f,la,n)
