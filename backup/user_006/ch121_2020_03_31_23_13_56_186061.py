def subtracao_de_listas(lista1, lista2)
    lista3=[]
    for i in lista1:
        if i not in lista2:
            lista3.append(i)
    return lista3