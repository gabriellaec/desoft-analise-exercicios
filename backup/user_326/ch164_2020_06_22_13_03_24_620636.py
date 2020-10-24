def traduz(list_eng, dic_eng2port):
    lista_traduzida = []
    for word in list_eng:
        lista_traduzida.append(dic_eng2port[word])
    return lista_traduzida