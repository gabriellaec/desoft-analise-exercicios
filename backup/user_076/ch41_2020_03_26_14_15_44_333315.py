def zera_negativos(lista):
    contador = 0
    tamanho = len (lista)
    while contador < tamanho:
        if lista[contador] < 0:
            lista [contador] == 0
            contador = contador + 1 
        else:
            lista [contador]  = lista  [contador]
            contador = contador +1
    return lista
        