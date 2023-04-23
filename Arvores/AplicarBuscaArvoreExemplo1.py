from NodoArvore import NodoArvore
from InsercaoArvore import insere
from BuscaArvore import busca
from Cont import Contador

# Cria uma árvore binária de pesquisa.
raiz = NodoArvore(40)
for chave in [5, 74, 20, 18, 55, 23, 94, 60, 8, 101, 84, 62, 50, 4, 42, 70, 12, 57, 10, 30]:
    nodo = NodoArvore(chave)
    insere(raiz, nodo)

cont = Contador()

# Procura por valores na árvore.
#[-50, 10, 30, 70, 101]
for chave in [-50, 10, 30, 70, 101]:
    resultado = busca(raiz, chave, cont)
    if resultado:
        print(f"Busca pela chave {chave}: Sucesso!")
    else:
        print(f"Busca pela chave {chave}: Falha!")

total = cont.getCont()
print(f'Executou {total} vezes.')
