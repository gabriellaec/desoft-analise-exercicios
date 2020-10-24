def traduz(lista_ing, dic_traduc):
    #recebo lista de palavras em ingles
    #recebo dic onde key= ingles e value= portugues
    #retorno lista c/ as traduções em portugues
    lista_lp = []
    for palavra in lista_ing:
        for ing, lp in dic_traduc.items():
            if palavra == ing:
                lista_lp.append(lp)
    return lista_lp