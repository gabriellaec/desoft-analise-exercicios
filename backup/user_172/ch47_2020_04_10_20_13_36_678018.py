def estritamente_crescente (lista):
    lista2 = []
    i = 0
    x = 1
    while lista[i+x]>lista[i]:
        lista2.append(lista[0])
        lista2.append(lista[i])
    return lista2