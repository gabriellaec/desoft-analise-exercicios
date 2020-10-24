def junta_listas(lista=[]):
    lista_final = []
    for i in lista:
        for j in i:
            lista_final.append(j)
    return lista_final