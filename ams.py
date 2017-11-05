# -*- coding:utf-8 -*-

import collections
import random
import numpy as np

max_ = 100000000000  # numero maximo que pode ser gerado


def generate_numbers():  # fresolve a questao 1

    numbers = []  # lista que e usada para gerar N8 numeros (o maximo que cabe na memoria)
    np.random.seed(50)  # semente para sempre gerar a msm sequencia de numeros

    for i in range(100):  # executa 100 vezes para poder a partir das listas de N8 formar um dicionario com N10
        numbers = np.random.uniform(0, 1, 1000000)
        numbers = np.square(numbers)
        numbers = np.floor(1 / numbers)
        numbers[numbers > max] = max_

    return numbers


def AMSestimate():
    sequence = generate_numbers()

    map_count = generate_map_count(sequence)
    return int(len(sequence) / float(len(map_count)) * sum((2 * v - 1) for v in map_count.values()))


def generate_map_count(sequence, num_samples=10):
    indexes = range(len(sequence))  # inicializa um vetor com indices
    random.shuffle(indexes)
    indexes = sorted(indexes[: num_samples])  # posicao de cada variavel aleatoria

    map_count = {}
    for index in indexes:
        counter = collections.Counter(sequence[index:])
        element = sequence[index]
        value = counter.get(element)
        map_count.update({element: value})
    return map_count


if __name__ == "__main__":
    print(AMSestimate())
