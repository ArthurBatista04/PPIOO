import time
def bubbleSort(alist):
    start = time.time()
    count = 0
    for passnum in range(len(alist)-1, 0, -1):
        for i in range(passnum):
            if alist[i] > alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
                count = count + 1
                yield [alist.copy(), time.time() - start, False, count]
    yield [alist.copy(),time.time() - start, True, count]
