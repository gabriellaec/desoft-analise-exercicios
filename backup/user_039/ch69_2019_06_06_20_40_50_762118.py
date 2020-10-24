def junta_listas(lista):
    listanova=[]
    for i in lista:
        for e in lista[i]:
            listanova.append(e)
    return listanova