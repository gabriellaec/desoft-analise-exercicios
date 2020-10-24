def junta_nome_sobrenome(lista1,lista2):
    lista3=[]
    i=0
    while len(lista1)>i:
        lista3.append(lista1[i])
        i+=1
    while len(lista2)>i:
        lista3.append(lista2[i])
    return lista3