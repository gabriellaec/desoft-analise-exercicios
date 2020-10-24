def interseccao_chaves(dict1, dict2):
    lista_interseccao = []
    lista_1 = []
    lista_2 = []
    for i in dict1.keys():
        lista_1.append(i)
    for e in dict2>keys():
        lista_2.append(e)
    for elemento in lista_1:
        if elemento in lista_2:
            lista_interseccao.append(elemento)
    return lista_interseccao