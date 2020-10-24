def numero_no_indice(lista):
    lista_ind=[]
    num_lista=len(lista)
    i = 0
    while i < num_lista:
        if lista[i] == i:
            lista_ind.append(lista[i])
            i+=1
        else:
            i+=1
    return lista_ind