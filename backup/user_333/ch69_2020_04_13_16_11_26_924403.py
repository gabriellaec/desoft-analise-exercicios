def junta_listas(lista):
    lista_final=[]
    for i in range(len(lista)):
        lista_i=lista[i]
        for e in range(lista_i):
            lista_final.append(lista_i[e])
    return lista_final
            
    