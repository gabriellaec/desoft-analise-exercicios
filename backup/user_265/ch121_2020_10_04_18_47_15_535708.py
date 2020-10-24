def subtracao_de_listas(lista1, lista2):
    i = 0
    nova=[]
    while i < len(lista1):
        if lista1[i] not in lista2:
            nova.append(lista1[i])
        i += 1
    return nova
