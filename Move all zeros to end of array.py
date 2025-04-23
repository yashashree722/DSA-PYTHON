def Move_all_zeros_to_end_of_array(arr):
    
    n =len(arr)
    cnt =0
    
    for i in range (n):
        if arr[i] != 0:
            arr[cnt] = arr[i]
            cnt = cnt+1 

    while cnt< n:
        arr[cnt] = 0 
        cnt = cnt+1
    
    
        
    
    
    
if __name__ =="__main__":
    # arr = [1,2, 0, 4, 3, 0, 5, 0]
    arr = [10 ,20,40,89]
    Move_all_zeros_to_end_of_array(arr)
    
    for num in arr:
        print(num, end=" ")