def estritamente_crescente(lista):
    i = 1
    maior = lista[0]
    listac = []
    listac.append(lista[0])
    if len(lista) == 0:
        return []
    while i < len(lista):
        if lista[i] > maior:
            maior = lista[i]
            listac.append(lista[i])
            i+=1
        else:
            i+=1
    return listac