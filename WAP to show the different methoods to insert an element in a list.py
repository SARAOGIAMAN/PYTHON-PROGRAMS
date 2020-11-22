n=int(input("Enter the size of the list:"))
list1=[]
for i in range(n):
    ele=int(input())
    list1.append(ele)    
print(list1)
list1.insert(2,10)
print(list1)
