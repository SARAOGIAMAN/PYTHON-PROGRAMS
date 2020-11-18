def repeat(n): 
    size=len(n) 
    repeated=[] 
    for i in range(size): 
        k=i+1
        for j in range(k,size): 
            if n[i]==n[j] and n[i] not in repeated: 
                repeated.append(n[i]) 
    return repeated
list1=[10,20,30,20,20,30,40,50,-20,60,60,-20,-20] 
print (repeat(list1))
