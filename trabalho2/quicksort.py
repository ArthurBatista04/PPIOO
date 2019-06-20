def partition(arr,low,high,order): 
    i = ( low-1 )          
    pivot = arr[high]      
    for j in range(low , high):  
        if arr[j] <= pivot: 
            i = i+1 
            arr[i],arr[j] = arr[j],arr[i]
    arr[i+1],arr[high] = arr[high],arr[i+1] 
    order.append(arr.copy())
    return ( i+1 ) 

def quickSort(arr,low,high,order): 
    if low < high: 
        pi = partition(arr,low,high,order) 
        quickSort(arr, low, pi-1,order) 
        quickSort(arr, pi+1, high,order) 