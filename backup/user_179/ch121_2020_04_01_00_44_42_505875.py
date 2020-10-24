def subtracao_de_listas (lista1, lista2):
    lista3 = []
    while i < len(lista1):
        i = 0
        if lista1[i] in lista2:
            i = i + 1
        else: 
            lista3[i] = lista1[i]
            i = i+1
    return lista3