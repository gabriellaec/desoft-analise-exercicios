def interseccao_chaves(dic_1, dic_2):
    lista_chaves = []
    for nome in dic_1.keys():
        lista_chaves.append(nome)
    for nome in dic_2.keys():
        if nome not in dic_1.keys():
            lista_chaves.append(nome)

    return lista_chaves