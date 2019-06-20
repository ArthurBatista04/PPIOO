import time
def bubbleSort(alist, order,algotime):
    start = time.time()
    for passnum in range(len(alist)-1, 0, -1):
        for i in range(passnum):
            if alist[i] > alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
                order.append(alist.copy())
                algotime.append(time.time() - start)
