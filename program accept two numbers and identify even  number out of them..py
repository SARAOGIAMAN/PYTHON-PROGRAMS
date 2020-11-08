a = int(input("Enter a: "))
b = int(input("Enter b: "))
if(a%2==0  and b%2==1):
print("a is even")
elif(b%2==0 and a%2==1):
print("b is even")
elif(a%2==0 and b%2==0):
print("Both are even")
else: 
print("Both are odd")
