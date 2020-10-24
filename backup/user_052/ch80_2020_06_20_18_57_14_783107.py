def interseccao_chaves (dicionario, dic):
    lista = []
    a = dicionario.keys()
    b = dic.keys()
    if a in b:
        lista.append(a)
    if b in a:
        lista.append(b)

    return lista
                