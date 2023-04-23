def busca(raiz, chave, cont):
    """Procura por uma chave em uma árvore binária de pesquisa."""
    # Trata o caso em que a chave procurada não está presente.
    if raiz is None:
        return None

    # A chave procurada está na raiz da árvore.
    if raiz.chave == chave:
        cont.incrementCont()
        return raiz,cont

    # A chave procurada é maior que a da raiz.
    if raiz.chave < chave:
        cont.incrementCont()
        return busca(raiz.direita, chave, cont)
    # A chave procurada é menor que a da raiz.
    else:
        cont.incrementCont()
        return busca(raiz.esquerda, chave, cont)

