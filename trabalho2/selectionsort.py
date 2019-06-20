import time
def selectionSort(A, order,algotime):
	start = time.time()
	for i in range(len(A)):
		min_idx = i
		swap = False
		for j in range(i+1, len(A)):
			if A[min_idx] > A[j]:
				min_idx = j
				swap = True
		A[i], A[min_idx] = A[min_idx], A[i]
		if swap:
			order.append(A.copy())
			algotime.append(time.time() - start)
