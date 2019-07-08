import time
def selectionSort(A):
	start = time.time()
	count = 0
	for i in range(len(A)):
		min_idx = i
		swap = False
		for j in range(i+1, len(A)):
			if A[min_idx] > A[j]:
				min_idx = j
				swap = True
		A[i], A[min_idx] = A[min_idx], A[i]
		if swap:
			count = count + 1
			yield [A.copy(),time.time() - start, False,count]
	yield [A.copy(),time.time() - start, True,count]