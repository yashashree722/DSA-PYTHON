def maxconsecutiveone(arr):
    n =len(arr)
    maxcount =0 
    currcnt =1
    
    for i in range(1,n):
        if arr[i] == arr[i-1]:
            currcnt = currcnt+1
        else :
            maxcount = max(maxcount, currcnt)
            currcnt =1 
    return max(maxcount, currcnt)
        

    
    
    
    
    
    
    
if __name__ == "__main__":
    arr = [0,0,0,0]
    print(maxconsecutiveone(arr))
    