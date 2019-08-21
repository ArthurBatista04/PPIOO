import os
import time
import random
from selectionsort import selectionSort
from bubblesort import bubbleSort
from insertionsort import insertionSort


def fillIntance(instance):
	element = [" " for i in range(len(instance))] 
	table = [element.copy() for i in range(len(instance))] # monta a tabela NxN (em que N correponde à quantidade de elementos no vetor a ser ordenado)
	for (line,element) in enumerate(instance):
		column = instance[line] - 1 #coluna correpondente do elemento
		table[line][column] = element # insere, para cada linha da matriz, o elemento na poiscao correpondendente. Exemplo: [1,2,3] -> [[1,"",""],["",2,""],["","",3]]
	return table	


def printInstance(instance,algorithmName,times,count):
	print('Nome: ' + algorithmName) # Nome do algoritmo 
	print('Tempo: ' + str(times)) # Tempo de execução naquele instante	
	print('Quantidade de trocas: ' + str(count)) # Quantidade de trocas até aquele instante
	for each_line in instance: # printa o vetor em formato matricial
		print()
		for each_numbers in each_line :	
			print(each_numbers, end=" ")
	print()

def printFinalInstance(finishedDetails,i): #printa as informações do algoritmo terminado
	table = fillIntance(finishedDetails[i]['instance'])
	printInstance(table,finishedDetails[i]['name'],str(finishedDetails[i]['time']),str(finishedDetails[i]['interations']))

def main():
	os.system('clear')
	print("Selecione as seguintes opções de vetor")
	print("1 - Aleatóiro\n2 - Invertido\n3 - Cresce e diminui")
	listOption = int(input("Digite a opção: ")) #escolha do vetor pelo usuário
	if listOption not in [1,2,3]: raise ValueError(listOption,' é uma opção inválida!')  

	if listOption == 1:
		inputList = random.sample(range(1,11),10) #lista de com 10 elementos randomicos
	elif listOption == 2:
		inputList = [x for x in range(10,0,-1)] #lista invertida
	else:
		inputList = [x for x in range(1,11,2)] #lista cresce 
		inputList.extend([x for x in range(10,1,-2)]) #lista decresce
	os.system('clear')

	algorithms = {0:{"BubbleSort": bubbleSort(inputList.copy())},1:{"SelectionSort":selectionSort(inputList.copy())},2:{"InsertionSort":insertionSort(inputList.copy())}} #algoritmos de ordenação
	numberOfAlgorithms = len(algorithms)#quantidade de algoritmos de ordenação
	finishedDetails = {}#informações dos algoritmos quando terminarem de executar
	userOptions = {} #algoritmos escolhidos pelo usuário

	numberOfUserAlgorithms = int(input("Digite a quantidade de algoritmos para serem simulados (max "+str(numberOfAlgorithms)+"): "))
	if numberOfUserAlgorithms not in range(1,numberOfAlgorithms+1): raise ValueError(numberOfUserAlgorithms,' é uma opção inválida!')  

	print("Selecione as seguintes opções")
	for i in algorithms:
		print(str(i) + " - " + list(algorithms[i].keys())[0]) #printa as opções de algoritmos para o usuário escolher

	for i in range(numberOfUserAlgorithms):
		op = int(input("Digite a opção: ")) #escolha de algoritmo pelo usuário
		if op not in userOptions and op in range(numberOfAlgorithms): #verifica se opção não é repitida e se é válida
			userOptions[op] = True
		else: raise ValueError(op,' é uma opção inválida ou repetida!')  
	os.system('clear')

	executionOption = int(input("Selecione 1-Full Simulation 2-Step by Step: ")) #Seleciona modo de simulação
	if executionOption not in [1,2]:raise ValueError(executionOption,' é uma opção inválida!')  
	os.system('clear')

	if executionOption == 1:
		while True: # enquanto todos os algoritmos não estiverem ordenados 
			for i in userOptions: # para cada opção que o usuário digitou
				if userOptions[i]: # verifica se o algoritmo não terminou
					algorithmName = list(algorithms[i].keys())[0] 
					instance,times,done,count = next(algorithms[i][algorithmName]) #retorna uma instância do algoritmo (com o vetor, tempo, booleano(terminado = true) e quantidade de trocas)
					if done: # se terminou
						finishedDetails[i] = {'time':times, 'name':algorithmName, 'interations' : count, 'instance': instance} # Insira no dicionário todos os dados de término dele
						userOptions[i] = False
					table = fillIntance(instance) #Constrói a matriz com base na instância
					printInstance(table,algorithmName,times,count) #Printa a matriz
				else: #caso o algoritmo tenha terminado
					printFinalInstance(finishedDetails,i)
			time.sleep(1) #espera 1 segundo
			os.system('clear')#limpa o terminal
			if not any(userOptions.values()):break #se todos os algoritmos terminarem
		os.system('clear')

	elif executionOption == 2:
		Input = input('Precione enter para continuar!')
		while not Input: #enquanto digitar enter
			os.system('clear')
			for i in userOptions:
				if userOptions[i]:
					algorithmName = list(algorithms[i].keys())[0]
					instance,times,done,count = next(algorithms[i][algorithmName]) 
					if done:
						finishedDetails[i] = {'time':times, 'name':algorithmName, 'interations' : count, 'instance': instance}
						userOptions[i] = False
					table = fillIntance(instance)
					printInstance(table,algorithmName,times,count)
				else: #caso o algoritmo tenha terminado
					printFinalInstance(finishedDetails,i)
			if not any(userOptions.values()):break
			Input = input('Precione enter para continuar!')
		os.system('clear')

	print("Informações finais!\n")
	for i in finishedDetails:
		printFinalInstance(finishedDetails,i)
if __name__ == '__main__':
	main()