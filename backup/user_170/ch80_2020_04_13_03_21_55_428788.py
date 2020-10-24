def interseccao_chaves(lista1, lista2):
    interseccao = []
    for i in lista1:
        if i in lista2:
            interseccao.append(i)
    return interseccao