def junta_nome_sobrenome(lista1,lista2):
    i = 0
    lista3 =[]
    while i < len(lista1):
        lista3.append('{0} {1}'.format(lista1[i],lista2[i]))
        i=i+1
    return lista3
