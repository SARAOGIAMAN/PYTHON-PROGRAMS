string1=input("Enter First String: ")
string2=input("Enter Second String:")
l1=len(string1)
l2=len(string2)
if(l2>l1):
    print("Not Possible")
else:
    f=string1.find(string2)
    if(f==-1):
        print("Not Possible")
    else:
        print("Yes")
