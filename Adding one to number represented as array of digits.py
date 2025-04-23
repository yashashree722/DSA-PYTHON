def fun(arr):
    
    carry = 1 
    for i in range(len(arr)-1 , -1 , -1):
        sum  = arr[i] + carry
        arr[i] = sum % 10
        carry = sum // 10 
        
    if carry:
            arr.insert(0, carry)
            
    return arr
            
            
            
if __name__ == '__main__' :
    arr = [1,4,3]
    ans = fun(arr)
    for i in ans :
        print( i , end=' ')
        