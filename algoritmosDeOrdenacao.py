import time
import psutil #calculo da cpu e memória
import os
inicio = time.time()
total_memory = psutil.virtual_memory().total
used_memory = psutil.virtual_memory().used
used_cpu = psutil.cpu_times().user
pid = os.getpid()
py = psutil.Process(pid)
memoryUse = py.memory_info()[0]/2.**30  # memory use in GB...I think

arquivo = open("Random_100000.csv",'r')
read = arquivo.read()
A = read.split("\n")
A.remove('')
A = list(map(int, A))

def bubble_sort1(lista):
    qtComp = 0
    qtTroca = 0
    elementos = len(lista)
    for j in range(elementos):
        for i in range(elementos-1):
            qtComp+=1 #vai pro if comparar
            if lista[i] > lista[i+1]:
                qtTroca+=1 #sempre que entrar no if faz a troca
                aux = lista[i]
                lista[i] = lista[i+1]
                lista[i+1] = aux
    print("Bubble Sort 1\nquantidade de comparações: ",qtComp, "\nquantidade de trocas:",qtTroca)
    #print(lista)

'''bubble_sort1(A)
fim = time.time()
print('Total da memória:',total_memory, "\nmemória utilizada",memoryUse,
      "\nCPU utilizada:",used_cpu, "\ntempo de execução",fim - inicio)'''

def bubble_sort2(lista):
    qtComp = 0
    qtTroca = 0
    elementos = len(lista)
    for j in range(elementos):
        for i in range(elementos-1, j, -1):
            qtComp+=1
            if lista[i] < lista[i-1]:
                qtTroca+=1
                aux = lista[i]
                lista[i] = lista[i-1]
                lista[i-1] = aux
    print("Bubble Sort 2\nquantidade de comparações: ",qtComp, "\nquantidade de trocas:",qtTroca)
    #print(lista)

bubble_sort2(A)
fim = time.time()
print('Total da memória:',total_memory, "\nmemória utilizada",used_memory,
      "\nCPU utilizada:",used_cpu, "\ntempo de execução",fim - inicio)

def bubble_sort3(lista):
    qtComp = 0
    qtTroca = 0
    elementos = len(lista)-1
    ordenado = False
    while not ordenado:
        ordenado = True
        for i in range(elementos):
            qtComp+=1
            if lista[i] > lista[i+1]:
                qtTroca+=1
                lista[i], lista[i+1] = lista[i+1],lista[i]
                ordenado = False        
                #print(lista)
    print("Bubble Sort 3\nquantidade de comparações: ",qtComp, "\nquantidade de trocas:",qtTroca)
    #print(lista)

'''bubble_sort3(A)
fim = time.time()
print('Total da memória:',total_memory, "\nmemória utilizada",used_memory,
      "\nCPU utilizada:",used_cpu, "\ntempo de execução",fim - inicio)'''

def insertionSort(A):
    qtComp = 0
    qtTroca = 0
    L = len(A)
    i = 2
    for i in range(1,L):
        eleito = A[i]
        j = i
        qtComp+=1
        while (j > 0) and (A[j-1] > eleito):
            qtTroca+=1
            A[j] = A[j-1]
            j = j - 1
        A[j] = eleito
    print("Insertion Sort \nquantidade de comparações: ",qtComp, "\nquantidade de trocas:",qtTroca)
    #print(lista)

'''insertionSort(A)
fim = time.time()
print('Total da memória:',total_memory, "\nmemória utilizada",used_memory,
      "\nCPU utilizada:",used_cpu, "\ntempo de execução",fim - inicio)'''


#A=[5,2,3,10,6,8,9]
def selectionSort(A):
   qtComp = 0
   qtTroca = 0
   L = len(A)
   for i in range(L-1):
      # print(i)
       eleito = A[i]
       menor = A[i+1]
       pos = i+1
       for j in range(i+1,L):
           qtComp+=1
           if A[j] < menor:
               qtTroca +=1
               menor = A[j]
               pos = j
       qtComp+=1
       if menor < eleito:
           qtTroca+=1
           A[i] = A[pos]
           A[pos] = eleito    
   print("Selection Sort \nquantidade de comparações: ",qtComp, "\nquantidade de trocas:",qtTroca)
   #print(lista)

'''selectionSort(A)
fim = time.time()
print('Total da memória:',total_memory, "\nmemória utilizada",used_memory,
      "\nCPU utilizada:",used_cpu, "\ntempo de execução",fim - inicio)'''
arquivo.close()
