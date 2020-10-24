def junta_nome_sobrenome(lista1,lista2):
    lista3=[]
    i=0
    while len(lista1)>i:
        lista3.append(lista1[i])
        lista3.append(lista2[i+1])
        i+=1
    return lista3