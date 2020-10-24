def simplifica_dict(dicionario):
    lista = []
    for chave in dicionario:
        if chave not in lista:
            lista.append(chave)
        for valor in dicionario[chave]:
            if dicionario[chave] not in lista:
                lista.append(dicionario[chave])

    return lista