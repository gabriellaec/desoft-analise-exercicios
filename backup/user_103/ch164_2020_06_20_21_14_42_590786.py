def traduz(lista_palavras, dicio_traduz):
    lista_traduzida =[]
    for i in range(len(lista_palavras)):
        for nome,trad in dicio_traduz.items():
            dicio_traduz[nome] = trad
            if lista_palavras[i] == nome:
                lista_traduzida.append(trad)
    return lista_traduzida