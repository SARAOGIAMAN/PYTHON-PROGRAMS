n=int(input("Enter the no of elements:"))
l1=[]
for i in range(n):
    ele=int(input())        
    l1.append(ele)
s1=set(l1)
print(s1)
print(sum(s1))
