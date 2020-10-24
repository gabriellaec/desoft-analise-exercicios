lista0 = []
i = 0
def subtracao_de_listas(lista1,lista2):
    while(i < len(lista1)):
        if lista1[i] in lista2:
            lista0.append(lista1[i])
            i += 1
    return lista0