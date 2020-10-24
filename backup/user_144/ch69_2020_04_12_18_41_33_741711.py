def junta_listas(lista):
    lista2 = []
    for i in range(len(lista)):
        for e in range(len(lista[i])):
            if lista[i][e] not in lista2:
                lista2.append(lista[i][e])
            
    return lista2