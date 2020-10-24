def interseccao_chaves(dicionario1,dicionario2):
    lista = []
    for chave1 in dicionario1.keys():
        for chave2 in dicionario2.keys():
            if chave1 == chave2:
                lista.append(chave1)
    return lista