def estritamente_crescente (lista):
    i = 0
    lista_crescente = []
    lista_crescente[0] = lista[0]
    while i < len(lista):
        if lista[i+1]>lista[i]:
            lista_crescente.append(lista[i+1])
        i+=1
    return lista_crescente