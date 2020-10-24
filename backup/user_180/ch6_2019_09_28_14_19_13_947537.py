def encontra_maximo(matriz):
    comparacoes = 0
    for lista in matriz:
        if comparacoes < lista.max():
            comparacoes = lista.max()
  	return comparacoes