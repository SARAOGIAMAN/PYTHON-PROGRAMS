string1=input("Enter the STRING:")
if(len(string1)<4):
    print("Not possible")
else:
    l=len(string1)
    s1=string1[0:3]
    s2=string1[4:l]
    print(s1+'h'+s2)
