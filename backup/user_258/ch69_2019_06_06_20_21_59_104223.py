def junta_listas(lista_listas):
    lista_final = []
    i=0
    while i < len (lista_listas):
        for k in range(0,len(lista_listas[i])):
            lista_final.append(lista_listas[i][k])
        i+=1
    return lista_final