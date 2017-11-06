# -*- coding: utf-8 -*-
"""
Spyder Editor

Este é um arquivo de script temporário.
"""

import random
import math
import numpy as np

max1 = 100000000000 # numero maximo que pode ser gerado


def generate_numbers():# fresolve a questao 1

    numbers=[] # lista que e usada para gerar N8 numeros (o maximo que cabe na memoria)
    map_count ={} # armazena os numeros distintos
    np.random.seed(50)# semente para sempre gerar a msm sequencia de numeros
	
    for i in range(100):# executa 100 vezes para poder a partir das listas de N8 formar um dicionario com N10
        numbers = np.random.uniform(0,1,100000000)
        numbers = np.square(numbers)
        numbers = np.floor(1/numbers)
        numbers[numbers>max1] = max1

        for n in np.unique(numbers):
            if n not in  map_count:
                map_count[n] = 1
           
    return map_count


def surpriser_number():# resolve a questao 3

    numbers=[] # lista que e usada para gerar N8 numeros (o maximo que cabe na memoria)
    map_count ={} # armazena as reptições de cada número do conjunto
    np.random.seed(50)# semente para sempre gerar a msm sequencia de numeros
    
    for i in range(100):# executa 100 vezes para poder a partir das listas de N8 formar um dicionario com N10
        numbers = np.random.uniform(0,1,100000000)
        numbers = np.square(numbers)
        numbers = np.floor(1/numbers)
        numbers[numbers > max1] = max1
        
        unique, counts = np.unique(numbers, return_counts=True)
        for i in range(len(unique)):
            number = unique[i]
            if (number not in map_count):
                map_count[number] = counts[i]
            else:
                map_count[number] += counts[i]
            
    sn = 0 # armazena o suprise number
    for i in map_count:
        sn +=  pow(map_count[i],2)
    print (sn)


def count_zeros(n):

    count_z = 0
    index = len(n) - 1
    while (index >= 0):
        if n[index].__contains__('0'):
            count_z = count_z + 1
        else:
            break
        index = index - 1
    return count_z


def randomHash(prime=2654435761):# funcao de hash usada na questao 2
	a,b = random.randint(0,prime), random.randint(0,prime)
	def f(x):
		return int ( ((a*x + b) % prime) )
	return f


def numbers_distincts(num): # resolve a questao 2, num representa a quantidade de funcoes de hash a serem aplicadas
      
    numbers=[] # lista que e usada para gerar N8 numeros (o maximo que cabe na memoria)
    map_count ={} # armazena os numeros distintos
    np.random.seed(50)# semente para sempre gerar a msm sequencia de numeros
	
    for i in range(100):# executa 100 vezes para poder a partir das listas de N8 formar um dicionario com N10
        numbers = np.random.uniform(0,1,10000000)
        numbers = np.square(numbers)
        numbers = np.floor(1/numbers)
        numbers[numbers>max1] = max1

        for n in numbers:
            map_count[n] = 1

    r = [] # armazena os maiores valores da quantidade de zeros obtido a partir do dicionario original aplicado as funcoes de hash
    max_value = 0 # armazena o valor do numero que obtem a maior quantidade de zeros antes do digito um dos valores gerados por cada hash (em binario)
    zeros = 0
    for i in xrange(num):
        r.append(0)
    hashes = [randomHash() for _ in range(num)]# gera funcoes de hash solicitadas e armazena numa lista 
    for key, value in  map_count.items():
       i = 0
       max_value = 0
       for hash in hashes:
           value_h = hash(key)# aplica os hashs a cada valor do dicionario original para prever os numeros distintos
           value_b = bin(value_h) # transforma os  valores  gerados pelo hash em binario
           zeros = count_zeros(value_b)# conta os zeros ate o primeiro digito 1
           max_value = zeros
           if (max_value) > r[i] :
               r[i] = max_value
           i+=1
    print (' size r:',len(r))
    return r


def median(list):

    list.sort()
    if len(list) % 2 == 0:
        n = len(list)
        median = (list[n / 2 - 1] + list[n / 2]) / 2
    else:
        median = list[len(list) / 2]

    return median


def median_average(div, list, size_groups): # size_groups deve ser um multiplo de log2 N, aproximadamente 33
    median_r = []
    start = 0
    k=1
    average = []

    if len(list)%div == 0:
      for i in range(0,div):
            end =( (len(list)/div) * k) -1
            count = 0
            for j in range(start, end):
                count = count +list[j];
            average .append(count/size_groups)
            start = end+1
            k = k+1
            end = ((len(list) / div) * k) - 1
    print (average)

    print ('mediana das medias: ',pow(2,median(average)))


if __name__ == "__main__":
    print (generate_numbers())
   #median_average(20,numbers_distincts(1320), 66) # calcula a media das medinas dos valores contidos em r, dividas em grupos, para poder prever a quantidade de numeros distintos
   # surpriser_number()