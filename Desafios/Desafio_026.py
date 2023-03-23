# Desenvolva um método que calcula o volume de uma esfera. Para tanto,
# pesquise como calcular o volume de uma esfera.
from typing import Any

raio = float(input('Digite o valor do raio da esfera(m): '))
PI_VALOR = 3.141592


def calcVolume_Esfera(raio):
    res = (4 / 3) * PI_VALOR * (raio ** 3)
    return res


volume = calcVolume_Esfera (raio)

print(f'O volume da esfera de raio {raio} é de {volume :.2f}')
