def estritamente_crescente(lista):
    contador = 1
    while contador < len(lista):
        if lista [contador] <= lista[contador-1]:
            del lista[contador]
    return lista
       