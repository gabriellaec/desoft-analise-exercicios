def subtracao_de_listas (lista1,lista2):
    listafinal = lista1
    for i in lista1:
        if i in lista2:
            listafinal.remove(i)
    return listafinal
