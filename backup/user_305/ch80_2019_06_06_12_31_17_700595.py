def interseccao_chaves(dic, dic2):
    lista = []
    for k in dic.keys():
        if k in dic2.keys():
        	lista.append(k)
    return lista
