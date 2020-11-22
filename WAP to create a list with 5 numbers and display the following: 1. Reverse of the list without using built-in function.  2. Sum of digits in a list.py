n=int(input("Enter the size of the list "))
list1=[]
for i in range(n):
    ele=int(input())
    list1.append(ele)
print(list1)
print(list1[::-1])
sum=0
for i in list1:
    sum+=i
print(sum)
