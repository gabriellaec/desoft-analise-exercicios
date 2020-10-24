def subtracao_de_listas(lista1,lista2):
    lista2=[]
    for i in lista1:
        if i not in lista2:
            lista2.append(i)
    for i in lista2:
        if i not in lista1:
            lista2.append(i)
    return lista2
    