def interseccao_chaves(dic1,dic2):
    lista = []
    for chave in dic1.keys():
        for chave2 in dic2.keys():
            if chave==chave2:
                lista.append(chave)
    return lista