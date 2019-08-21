import os
import time
import random
from selectionsort import selectionSort
from bubblesort import bubbleSort
from insertionsort import insertionSort
from main import fillIntance

def testsPrints():
    arr = [5, 3, 2, 4, 1]

    assert (fillIntance(arr) == [[' ', ' ', ' ', ' ', 5], [' ', ' ', 3, ' ', ' '], [' ', 2, ' ', ' ', ' '], [' ', ' ', ' ', 4, ' '], [1, ' ', ' ', ' ', ' ']])
    assert (fillIntance(next(selectionSort(arr))) == [[1, ' ', ' ', ' ', ' '], [' ', ' ', 3, ' ', ' '], [' ', 2, ' ', ' ', ' '], [' ', ' ', ' ', 4, ' '], [' ', ' ', ' ', ' ', 5]])
    assert (fillIntance(next(selectionSort(arr))) == [[1, ' ', ' ', ' ', ' '], [' ', 2, ' ', ' ', ' '], [' ', ' ', 3, ' ', ' '], [' ', ' ', ' ', 4, ' '], [' ', ' ', ' ', ' ', 5]])

    arr = [5, 3, 2, 4, 1]

    assert (fillIntance(arr) == [[' ', ' ', ' ', ' ', 5], [' ', ' ', 3, ' ', ' '], [' ', 2, ' ', ' ', ' '], [' ', ' ', ' ', 4, ' '], [1, ' ', ' ', ' ', ' ']])
    assert (fillIntance(next(insertionSort(arr))) == [[' ', ' ', ' ', ' ', 5], [' ', ' ', ' ', ' ', 5], [' ', 2, ' ', ' ', ' '], [' ', ' ', ' ', 4, ' '], [1, ' ', ' ', ' ', ' ']])
    assert (fillIntance(next(insertionSort(arr))) == [[' ', ' ', ' ', ' ', 5], [' ', ' ', ' ', ' ', 5], [' ', ' ', ' ', ' ', 5], [' ', ' ', ' ', 4, ' '], [1, ' ', ' ', ' ', ' ']])

