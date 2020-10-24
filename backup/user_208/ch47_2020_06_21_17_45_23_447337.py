def estritamente_crescente (lista):
    i = 0
    lista1 = []
    while i < len(lista):
        if i == 0:
            lista1.append(lista[0])
        if i != 0:
            if lista[i] > lista[i-1]:
                lista1.append(lista[i])
        i+=1
    return lista1
        