def estritamente_crescente(lista):
    listaC = []
    listaC.append(lista[1])
    i = 1
    while i < len(lista):
        if lista[i] > lista[i-1]:
            listaC.append(lista[i])
    return listaC