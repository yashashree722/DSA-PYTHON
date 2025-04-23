def Reverse_array(arr, start ,end):
    while start <end:
        arr[start] , arr[end] = arr[end] , arr[start]
        start = start +1
        end = end -1

def Rotate_array_by_d(arr,k) :
    n= len(arr)
    k %= n
    
    
    Reverse_array(arr,0,d-1)
    Reverse_array(arr,d,n-1)
    Reverse_array(arr,0,n-1)
    
    
        
        
        
if __name__ =='__main__':
    arr= [1,2,3,4,5,6]
    d =2
    Rotate_array_by_d(arr,d)
    for i in arr:
        print(i ,end=' ')
    



    