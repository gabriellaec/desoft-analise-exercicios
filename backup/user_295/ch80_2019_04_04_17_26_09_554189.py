def interseccao_chaves (dic_1, dic_2):
    lista = []
    
    for chave_1, indice_1 in dic_1 .items():
        i = 0
        if chave_1 == dic_2[i]:
            lista.append(chave_1)
            i += 1
    return lista   