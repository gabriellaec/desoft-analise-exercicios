def separa_trios(lista):
    nova_lista = []
    lista_intermediaria = []
    for x in lista:
        lista_intermediaria.append(x)
        if len(lista_intermediaria) == 3:
            nova_lista.append(lista_intermediaria)
            lista_intermediaria = []
    if lista_intermediaria != []:
        nova_lista.append(lista_intermediaria)
    return nova_lista
        