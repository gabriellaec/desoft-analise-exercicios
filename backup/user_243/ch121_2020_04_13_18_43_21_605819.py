def subtracao_de_listas(lista1,lista2):
    lista2=[]
    for i in lista1:
        if i in not lista2:
            lista2.append(i)
    for i in lista2:
        if i in not lista1:
            lista2.append(i)
    return lista2
    