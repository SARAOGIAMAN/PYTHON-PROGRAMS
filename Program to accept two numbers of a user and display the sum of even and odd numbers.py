evensum=0
oddsum=0
a=int(input("Enter first no. "))
b=int(input("Enter second no. "))
for i in range(a,b+1):
    if i%2==0:
        evensum+=i
    else:
        oddsum+=i
print("Sum of even nos. ",evensum)
print("Sum of odd nos. ",oddsum)
