import time
def heapify(arr, n, i,order,algotime,start): 
    largest = i 
    l = 2 * i + 1     
    r = 2 * i + 2     
    if l < n and arr[i] < arr[l]: 
        largest = l 
    if r < n and arr[largest] < arr[r]: 
        largest = r 
    if largest != i: 
        arr[i],arr[largest] = arr[largest],arr[i] # swap 
        order.append(arr.copy())
        algotime.append(time.time() - start)
        heapify(arr, n, largest,order,algotime,start) 
def heapSort(arr,order,algotime):
    start = time.time() 
    n = len(arr) 
    for i in range(n, -1, -1): 
        heapify(arr, n, i,order,algotime,start) 
    for i in range(n-1, 0, -1): 
        arr[i], arr[0] = arr[0], arr[i] # swap 
        order.append(arr.copy())
        algotime.append(time.time() - start)
        heapify(arr, i, 0,order,algotime,start) 