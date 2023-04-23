from NodoArvore import NodoArvore
from OrdenacaoArvore import em_ordem

raiz = NodoArvore(40)

raiz.esquerda = NodoArvore(20)
raiz.direita  = NodoArvore(60)

raiz.direita.esquerda  = NodoArvore(50)
raiz.direita.direita   = NodoArvore(70)
raiz.esquerda.esquerda = NodoArvore(10)
raiz.esquerda.direita  = NodoArvore(30)

em_ordem(raiz)
