def inverte_lista(lista):
    i = 0
    listareversa = []
    while i<len(lista):
        listareversa.append(lista[len(lista-i)])
        i+=1
    return listareversa