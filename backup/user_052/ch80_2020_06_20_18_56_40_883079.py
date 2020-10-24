def interseccao_chaves (dicionario, dic):
    lista = []
    a = dicionario.keys()
    b = dic.keys()
    if a in dic:
        lista.append(a)
    if b in dicionario:
        lista.append(b)

    return lista
                