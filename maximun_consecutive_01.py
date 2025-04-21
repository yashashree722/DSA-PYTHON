# def maxconsecutiveone(arr):
#     n =len(arr)
#     maxcount =0 
#     currcnt =1
    
#     for i in range(1,n):
#         if arr[i] == arr[i-1]:
#             currcnt = currcnt+1
#         else :
#             maxcount = max(maxcount, currcnt)
#             currcnt =1 
#     return max(maxcount, currcnt)
        

    
    
    
#  another approch is using bit manipulation
def maxconsecutiveone (arr):
    
    maxele = 0
    currcnt = 1 
    prev = -1 
    
    for i in arr :
        if i^prev==0:
            currcnt = currcnt +1
        else :
            maxele = max(maxele, currcnt)
            currcnt =1 
        prev = i 
    return max(maxele, currcnt)
    
    
if __name__ == "__main__":
    arr = [0,0,0,0]
    print(maxconsecutiveone(arr))
    