def junta_listas(lista):
    lista_final = []
    for i in lista:
        lista2 = lista[i]
        for j in lista2:
            lista_final.append(j)
    return lista_final