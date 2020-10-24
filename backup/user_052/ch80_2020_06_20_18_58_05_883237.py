def interseccao_chaves (dicionario, dic):
    lista = []
    a = dicionario.keys()
    b = dic.keys()
    while i < len(dicionario):
        if a in b:
            lista.append(a)
            i += 1 
        elif b in a:
            lista.append(b)
            i += 1
        else:
            i += 1

    return lista