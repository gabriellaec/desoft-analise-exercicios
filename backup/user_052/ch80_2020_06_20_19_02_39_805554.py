def interseccao_chaves (dicionario, dic):
    lista = []
    for o in dic:
        if o in dicionario:
            lista.append(o)
    
    return lista