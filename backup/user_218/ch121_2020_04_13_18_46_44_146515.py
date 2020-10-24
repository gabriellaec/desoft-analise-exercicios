def subtracao_de_lista(lista1, lista2):
    lista = []
    for t in lista1:
        if t not in lista2:
            lista.append(t)
    return lista