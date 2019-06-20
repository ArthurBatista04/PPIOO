import os
import time
from selectionsort import selectionSort
from bubblesort import bubbleSort
from quicksort import quickSort, partition
import random



def inicialize(graph):
	element = [" " for i in range(len(graph))]
	graph = [element.copy() for i in range(len(graph))]
	return graph


def alterGraph(graph, order):
	for i in range(len(order)):
		graph[i][order[i]-1] = order[i]


def printInstance(graph):
	for inter in graph:
		print()
		for j in inter:
			print(j, end=" ")
	print()

quantalgoritmos = 3
quan = int(input("Digite a quantidade de algoritmos para serem simulados: "))
options = []
for i in range(quan):
	op = int(input("Selecione 0-BubbleSort 1-SelectionSort 2-QuickSort: "))
	options.append(op)

assert(quan > 0)

order = [[] for i in range(quantalgoritmos)]
graph = [[] for i in range(quantalgoritmos)]

notOrdered = random.sample(range(1,21), 20)
print(notOrdered)

for op in range(len(options)):
	if options[op] == 0:
		bubbleSort(notOrdered.copy(), order[options[op]])
	elif options[op] == 1:
		selectionSort(notOrdered.copy(), order[options[op]])
	elif options[op] == 2:
		quickSort(notOrdered.copy(),0,len(notOrdered)-1, order[options[op]])

max = 0
values = {}

for i in options:
	values[i] = len(order[i])
	if len(order[i]) > max:
		max = len(order[i])





for i in range(max):
	for op in options:
		if order[op]:	
			if op == 0:print("BUBBLE SORT\n")
			elif op == 1:print("SELECTION SORT\n")
			else:print("QUICK SORT\n")
			if i < values[op]:
				graph[op] = inicialize(notOrdered.copy())
				alterGraph(graph[op], order[op][i])	
			printInstance(graph[op])
	time.sleep(1)
	os.system("clear")		
