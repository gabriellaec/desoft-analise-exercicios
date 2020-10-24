def traduz(lista, dicionario):

    lista_traduzida = []

    for palavra in lista:
        for chave in dicionario:
            if palavra == chave:
                lista_traduzida.append(dicionario[chave])
    
    return lista_traduzida