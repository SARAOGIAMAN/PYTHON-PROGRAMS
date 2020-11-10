a = int(input("Enter number 1: "))
b = int(input("Enter number 2: "))
c = int(input("Enter number 3: "))
if(a==b and b==c):
print("1st prize")
elif(a==b and b!=c or a==c and b!=c):
print("2nd prize")
else:
print("3rd prize")	
