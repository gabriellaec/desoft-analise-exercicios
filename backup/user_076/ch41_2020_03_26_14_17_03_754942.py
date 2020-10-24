def zera_negativos(lista):
    contador = 0
    tamanho = len (lista)
    while contador < tamanho:
        if lista[contador] < 0:
            lista [contador] == 0
            contador = contador + 1 
    if contador == tamanho:
        return lista
        