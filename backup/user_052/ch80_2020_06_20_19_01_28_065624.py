def interseccao_chaves (dicionario, dic):
    lista = []
    i = 0
    while i < len(dicionario):
        for o in dic:
            if dic[o] in dicionario:
                lista.append(o)
                i += 1
            else:
                i += 1
    return lista