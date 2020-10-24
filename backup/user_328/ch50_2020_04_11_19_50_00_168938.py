def junta_nome_sobrenome(lista, lista2):
    x= len(lista)
    i=0
    listanova= [0]*x
    while i != x:
        listanova[i]= ' '.join(lista[i], lista2[i])
        i += 1
    return listanova