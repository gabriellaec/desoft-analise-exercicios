def interseccao_chaves(dicionario1,dicionario2):
    lista_de_chaves = []
    chaves1 = dicionario1.keys()
    chaves2 = dicionario2.keys()
    for chave in chaves1 :
        if chave in chaves2:
            lista_de_chaves.append(chave)
    return lista_de_chaves
            