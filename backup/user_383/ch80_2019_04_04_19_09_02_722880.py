def interseccao_chaves(dicionario1,dicionario2):
    lista_vazia = []
    for k1 in dicionario1.keys():
        if k1 in dicionario2:
            lista_vazia.append(k1)

    return lista_vazia