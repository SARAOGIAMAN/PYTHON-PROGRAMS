def remarr(arr,n):
    product=1
    for i in range(0,n):
        product=product*arr[i]
    rem=product%10
    return rem
arr=[1,2,3,4]
n=len(arr)
print(remarr(arr,n))
