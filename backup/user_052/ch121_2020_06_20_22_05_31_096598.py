def subtracao_de_listas (lista, lista2):
    nova = []
    for i in lista:
        if i in lista2:
            nova.append(i)
    return nova