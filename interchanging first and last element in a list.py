def swaplist(lis):
    n=len(lis)
    temp=lis[n-1]
    lis[n-1]=lis[0]
    lis[0]=temp
    return lis
lis=[1,2,3,4,5]
print(swaplist(lis))
