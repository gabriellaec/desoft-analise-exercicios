def subtracao_de_listas(lista1, lista2):
    lista3 = []
    for e in lista1:
        if e in lista2:
            lista3.append(e)
    return lista3
    