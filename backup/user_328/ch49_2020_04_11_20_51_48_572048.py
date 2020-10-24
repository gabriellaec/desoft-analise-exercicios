def inverte_lista(lista):
    x= len(lista)
    i=0
    indice= x
    listanova= [0]*x
    while i != x:
        listanova[i]= lista[indice-1]
        i += 1
        indice -= 1
    return listanova