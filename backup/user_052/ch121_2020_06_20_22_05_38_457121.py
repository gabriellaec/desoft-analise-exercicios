def subtracao_de_listas (lista, lista2):
    nova = []
    for i in lista2:
        if i in lista:
            nova.append(i)
    return nova