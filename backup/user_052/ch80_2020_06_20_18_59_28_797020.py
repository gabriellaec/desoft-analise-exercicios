def interseccao_chaves (dicionario, dic):
    lista = []
    i = 0
    while i < len(dicionario):
        if dicionario.keys in dic:
            if dic.keys in dicionario:
                lista.append(i)
                i += 1
    return lista