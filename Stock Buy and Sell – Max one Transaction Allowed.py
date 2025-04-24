def fun(arr) :
    minsofar = arr[0]
    
    res =0 
    for i in range (1 , len(arr)):
        minsofar = min(minsofar, arr[i])
        res = max(res , arr[i] -minsofar)
    return res 

if __name__ =='__main__' :
    arr = [1, 3, 6, 9, 11]
    ans = fun(arr)
    print(ans)