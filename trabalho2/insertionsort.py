from time import time
def insertionSort(arr): 
    start = time()
    count = 0
    for i in range(1, len(arr)): 
        key = arr[i]  
        j = i-1
        while j >=0 and key < arr[j] : 
            arr[j+1] = arr[j] 
            j -= 1
            count+=1
            yield [arr.copy(),time() -  start, False, count]
        arr[j+1] = key 
    yield [arr.copy(),time() -  start, True,count]   