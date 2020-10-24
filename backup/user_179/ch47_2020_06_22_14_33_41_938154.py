def estritamente_crescente(lista):
    lista2 = []
    for i in range(len(lista)):
        if i == 0:
            lista2.append(lista[i])
        else:
            if lista[i] > lista[i-1]:
                lista2.append(lista[i])
    return lista2