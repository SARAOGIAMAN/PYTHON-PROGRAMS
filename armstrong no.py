n=int(input("enter a no. "))
sum=0
new=n   
while n>0:
    d=n%10
    sum=sum+(d*d*d)
    n=n//10
if(sum==new):
    print("Armstrong ")
else:
    print("not armstrong")
