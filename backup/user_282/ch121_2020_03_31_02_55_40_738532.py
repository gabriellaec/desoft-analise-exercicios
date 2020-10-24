def subtracao_de_listas(lista1, lista2):
    lista = []
    for e in lista1:
        if e not in lista2:
            lista.append(e)
    return lista
