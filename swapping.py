def swaplist(lis,po1,po2):
    n=len(lis)
    temp=lis[po2]
    lis[po2]=lis[po1]
    lis[po1]=temp
    return lis
lis=[1,2,3,4,5]
po1=int(input("enter 1st position "))
po2=int(input("enter 2nd position "))
print(swaplist(lis,po1-1,po2-1))
