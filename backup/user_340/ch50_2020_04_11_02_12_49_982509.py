def junta_nome_sobrenome(lista1, lista2):
    lista3=[]
    i=0
    while i<len(lista1):
        a=lista1[i]
        b=lista2[i]
        c='{0} {1}'.format(a, b)
        lista3.append(c)
        i+=1
    return lista3