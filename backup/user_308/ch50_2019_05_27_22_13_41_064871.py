def numero_no_indice(lista):
    listeras=[]
    for e in range(len(lista)):
        if e==lista[e]:
            listeras.append(e)
    return listeras