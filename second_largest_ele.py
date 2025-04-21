def getSecondLargest(arr):
    n = len(arr)
    largest = -1 
    second_largest = -1 
    
    for i in range(n):
        if arr[i]> largest:
            second_largest = largest
            largest = arr[i]
            
        elif arr[i]> second_largest and arr[i] < largest:
            second_largest = arr[i]
        
    return second_largest



if __name__ == "__main__":
    arr = [12, 350, 1, 10, 34, 100]
    print(getSecondLargest(arr))
    
    
    