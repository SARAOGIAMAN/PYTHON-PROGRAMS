n=int(input("Enter the no. of items in dictionary:"))
d={}
for i in range(n):
    key=input("Enter the key: ")
    val=int(input("Enter the value: "))
    if(key.isnumeric()!=True and len(key)<=6 and val%2==0):
        d[key]=val
print(d)
