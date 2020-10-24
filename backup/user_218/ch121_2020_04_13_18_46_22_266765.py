def subtracao_de_lista(lista1, lista2):
    lista = []
    for a in lista1:
        if a not in lista2:
            lista.append(a)
    return lista