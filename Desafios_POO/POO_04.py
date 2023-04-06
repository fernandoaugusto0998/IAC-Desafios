# POO_04 - Crie um programa que sorteie e liste um determinado número de
# funcionários. Por exemplo, sortear aleatoriamente e listar 5 funcionários, SEM
# REPETIR.

import random
from FakeDB import FakeDB


fakeDB = FakeDB()
numSorteio = 5

print(f'\nLista de {numSorteio} Funcionarios selecionados aleatóriamente:')

sorteio = (random.sample(fakeDB.Funcionarios, numSorteio))

for i in sorteio:
    print(f'{i.getNome()}')