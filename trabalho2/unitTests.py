import os
import time
import random
from selectionsort import selectionSort
from bubblesort import bubbleSort
from insertionsort import insertionSort


def assertChanges():
    arr = [5, 3, 2, 4, 1]
    # retorna um vetor com a instancia, na posição 0 está o vetor
    output = next(selectionSort(arr))
    assert (output[0] == [1, 3, 2, 4, 5])
    output = next(selectionSort(arr))
    assert (output[0] == [1, 2, 3, 4, 5])
    output = next(selectionSort(arr))
    assert (output[0] == [1, 2, 3, 4, 5])

    arr = [5, 3, 2, 4, 1]
    output = next(bubbleSort(arr))
    assert (output[0] == [3, 5, 2, 4, 1])
    output = next(bubbleSort(arr))
    assert (output[0] == [3, 2, 5, 4, 1])
    output = next(bubbleSort(arr))
    assert (output[0] == [2, 3, 5, 4, 1])
    output = next(bubbleSort(arr))
    assert (output[0] == [2, 3, 4, 5, 1])
    output = next(bubbleSort(arr))
    assert (output[0] == [2, 3, 4, 1, 5])
    output = next(bubbleSort(arr))
    assert (output[0] == [2, 3, 1, 4, 5])
    output = next(bubbleSort(arr))
    assert (output[0] == [2, 1, 3, 4, 5])
    output = next(bubbleSort(arr))
    assert (output[0] == [1, 2, 3, 4, 5])

    arr = [5, 3, 2, 4, 1]
    output = next(insertionSort(arr))
    assert (output[0] == [3, 5, 2, 4, 1])
    output = next(insertionSort(arr))
    assert(output[0] == [3, 2, 5, 4, 1])
    output = next(insertionSort(arr))
    assert(output[0] == [2, 3, 5, 4, 1])
    output = next(insertionSort(arr))
    assert(output[0] == [2, 3, 4, 5, 1])
    output = next(insertionSort(arr))
    assert(output[0] == [2, 3, 4, 1, 5])
    output = next(insertionSort(arr))
    assert(output[0] == [2, 3, 1, 4, 5])
    output = next(insertionSort(arr))
    assert(output[0] == [2, 1, 3, 4, 5])
    output = next(insertionSort(arr))
    assert(output[0] == [1, 2, 3, 4, 5])


assertChanges()
