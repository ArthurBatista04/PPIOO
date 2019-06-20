import time
def partition(arr,low,high,order,algotime): 
	start = time.time()
	i = ( low-1 )          
	pivot = arr[high]      
	for j in range(low , high):  
		if arr[j] <= pivot: 
			i = i+1 
			arr[i],arr[j] = arr[j],arr[i]
	arr[i+1],arr[high] = arr[high],arr[i+1] 
	order.append(arr.copy())
	algotime.append(time.time() - start)
	return ( i+1 ) 

def quickSort(arr,low,high,order,algotime): 
	if low < high: 
		pi = partition(arr,low,high,order,algotime) 
		quickSort(arr, low, pi-1,order,algotime) 
		quickSort(arr, pi+1, high,order,algotime) 