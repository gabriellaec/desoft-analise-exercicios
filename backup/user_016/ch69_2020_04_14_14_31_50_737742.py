def junta_listas(lista):
    lista2 = []
    for i in range(len(lista)):
        x = lista[i]
        for u in range(len(x)):
            lista2.append(x[u])
    return lista2
            
    