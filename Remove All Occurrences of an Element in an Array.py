def fun(arr,k):
    k =0 
    
    n = len(arr)
    for i in range (n):
        if arr[i]!=k:
            arr[k] = arr[i]
            
            
            k = k+1
    return k

arr = [0, 1, 3, 0, 2, 2, 4, 2]
ele = 2
ans =fun(arr, ele)
print(ans)
