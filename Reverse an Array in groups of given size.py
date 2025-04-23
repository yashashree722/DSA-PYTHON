def Reverce_array_k_group(arr,k):
    n = len(arr)
    i =0 
    
    while i <n :
        left = i 
        right = min(i+k-1 , n-1)
        
        while left <right:
            arr[left] , arr[right] = arr[right] , arr[left]
            left = left+1
            right =right -1 
            
        i = i+k        
        
if __name__ =='__main__':
    arr= [1, 2, 3, 4, 5, 6, 7, 8] 
    k = 3
    Reverce_array_k_group(arr , k)
    for num in arr:
        print(num, end= ' ')