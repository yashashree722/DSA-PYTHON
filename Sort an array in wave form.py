# Approch 1 
def Sort_an_array_in_wave_form(arr,n):
    arr.sort()
    for i in  range (0,n-1 , 2) :
        arr[i] , arr[i+1] = arr[i+1] , arr[i]
        
  
    #   Apprich 2 
def Sort_an_array_in_wave_form(arr,n):
    for i in range (0, n,2):
        if (i>0 and arr[i] < arr[i-1]):
            arr[i] , arr[i-1] = arr[i-1] , arr[i]
        elif  (i<n-1 and arr[i] < arr[i+1]) :
             arr[i] , arr[i+1] = arr[i+1] , arr[i]
    



if __name__ =="__main__" :
    arr = [10, 90, 49, 2, 1, 5, 23]
    n = len(arr)
    Sort_an_array_in_wave_form(arr,n)
    for i in arr :
        print(i , end=' ')
