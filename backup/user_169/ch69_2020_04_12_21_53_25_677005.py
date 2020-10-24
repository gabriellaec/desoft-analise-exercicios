def junta_listas(lista):
    lista2=[]
    for i in range(len(lista)):
        for e in lista[i]:
            lista2.append(e)
    return lista2