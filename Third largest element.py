def getThirdLargest(arr):
    n = len(arr)
    first = second = third = float('-inf')
    for i in range(n):
        if arr[i] >first:
            third = second
            second = first
            first = arr[i]
        elif arr[i] > second and arr[i] <first :
            third = second
            second = arr[i]
        else : 
            third = arr[i]
    return third
    
    



if __name__== "__main__":
    arr = [1, 14, 2, 16, 10, 20]
    print(getThirdLargest(arr))
    