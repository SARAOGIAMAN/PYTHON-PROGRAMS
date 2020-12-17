def fact(n):
    f=1
    for i in range(n,0,-1):
        f*=i
    return f

n=int(input())
res=fact(n)
print(res)
