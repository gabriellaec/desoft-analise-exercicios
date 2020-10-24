def subtracao_de_listas (lista1, lista2):
    lista3 = []
    i = 0
    while i < len(lista1):
        if lista1[i] in lista2:
            i = i + 1
        else:
            lista3.append(lista1[i])
            i = i + 1