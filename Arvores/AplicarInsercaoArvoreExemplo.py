from NodoArvore import NodoArvore
from OrdenacaoArvore import em_ordem
from InsercaoArvore import insere

# Cria uma árvore binária de pesquisa.
raiz = NodoArvore(40)
for chave in [5, 74, 20, 18, 55, 23, 94, 60, 8, 101, 84, 62, 50, 4, 42, 70, 12, 57, 10, 30]:
    nodo = NodoArvore(chave)
    insere(raiz, nodo)
# Imprime o caminhamento em ordem da árvore.
em_ordem(raiz)
