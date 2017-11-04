import random
import math
import numpy as np

max_ = 100000000000 # número máximo que pode ser gerado


def generate_numbers():# fresolve a questao 1

    numbers=[] # lista que é usada para gerar N^8 números (o máximo que cabe na memoria)
    map_count ={} # armazena os numeros distintos
    np.random.seed(50)# semente para sempre gerar a msm sequencia de numeros
	
    for i in range(100):# executa 100 vezes para poder a partir das listas de N^8 formar um dicionario com N^10
        numbers = np.random.uniform(0,1,100000000)
        numbers = np.square(numbers)
        numbers = np.floor(1/numbers)
        numbers[numbers>max] = max_

        for n in np.unique(numbers):
            if n not in  map_count:
                map_count[n] = 1
    return map_count
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

def numbers_distincts(num): # resolve a questao 2, num representa a quantidade de funções de hash a serem aplicadas
    map_count = generate_numbers()
    print 'Quantidade de números distintos real:', map_count.__len__()

    r = [] # armazena os maiores valores da quantidade de zeros obtido a partir do dicionario original aplicado as funções de hash
    max_value = 0 # armazena o valor do número que obtem a maior quantidade de zeros antes do digito um dos valores gerados por cada hash (em binário)
    zeros = 0
    for i in xrange(num):
        r.append(0)
    hashes = [randomHash() for _ in range(num)]# gera funções de hash solicitadas e armazena numa lista 
    for key, value in  map_count.items():
       i = 0
       max_value = 0
       for hash in hashes:
           value_h = hash(key)# aplica os hashs a cada valor do dicionario original para prever os números distintos
           value_b = bin(value_h) # transforma os  valores  gerados pelo hash em binario
           zeros = count_zeros(value_b)# conta os zeros até o primeiro digito 1
           max_value = zeros
           if (max_value) > r[i] :
               r[i] = max_value
           i+=1



    median_average(20,r) # calcula a media das medinas dos valores contidos em r, dividas em grupos, para poder prever a quantidade de numeros distintos



def median(list):

    list.sort()
    if len(list) % 2 == 0:
        n = len(list)
        mediana = (list[n / 2 - 1] + list[n / 2]) / 2
    else:
        mediana = list[len(list) / 2]

    return mediana

def median_average(div, list):
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
            average .append(count/33)
            start = end+1
            k = k+1
            end = ((len(list) / div) * k) - 1
    print average

    print 'mediana das medias: ',pow(2,median(average))


if __name__ == "__main__":
   numbers_distincts(660)