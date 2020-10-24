def subtracao_de_listas(lista1, lista2):
    lista =[]
    i = 0
    while i<len(lista1):
        j=0
        while j<len(lista2):
            if lista1[i]==lista2[j]:
                break
            j += 1
        if j == len(lista2):
            lista.append(lista1[i])
        i += 1
    return lista
