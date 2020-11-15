a=int(input(“Enter the First number ”))
b=int(input(“Enter the second number ”))
for i in range(a,b):
    for j in range(2,i):
        if(i%j)==0:
            break
    else:
        print(i)
