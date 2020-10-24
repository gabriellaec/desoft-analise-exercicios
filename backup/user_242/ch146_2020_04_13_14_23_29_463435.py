def conta_ocorrencias(lista_de_palavras):
    dic = {}
    for palavra in lista_de_palavras:
        dic[palavra] = lista_de_palavras.count(palavra)
        
    return(dic)   