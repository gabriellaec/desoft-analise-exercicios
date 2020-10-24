def subtracao_de_listas (lista1,lista2):
    i = 0
    c = 0
    while i < len(lista1):
        if lista1[i] in lista2:
            del lista1[i]
        i+=1
    return lista1