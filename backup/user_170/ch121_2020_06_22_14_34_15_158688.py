def subtracao_de_listas(lista1, lista2):
    newLs = []
    for i in lista1:
        if i not in lista2:
            newLs.append(i)
    return newLs