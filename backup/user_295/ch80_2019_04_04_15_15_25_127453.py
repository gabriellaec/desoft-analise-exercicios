def interseccao_chaves (dic_1, dic_2):
    lista = []
    for chave,indice in dic_1 .items():
        lista.append(chave)
    for c,i in dic_2 .items():
        lista.append(c)
    return lista   