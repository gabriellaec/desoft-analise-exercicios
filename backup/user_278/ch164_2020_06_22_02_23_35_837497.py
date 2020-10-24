def traduz(lista_ing, dic_traduc):
    #recebo lista de palavras em ingles
    #recebo dic onde key= ingles e value= portugues
    #retorno lista c/ as traduções em portugues
    lista_lp = []
    for ing, lp in dic_traduc.items():
        for palavra in lista_ing:
            if palavra == ing:
                lista_lp.append(lp)
    return lista_lp