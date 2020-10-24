def subtracao_de_listas(lista1,lista2):
    nova_lista = []
    i = 0
    while i <len(lista1):
        if lista1[i] not in lista2:
            nova_lista.append(lista[i])
        i += 1
    return nova_lista