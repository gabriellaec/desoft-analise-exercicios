def simplifica_dict (dicionario):
    ListaSemRepeticao = []
    
    #Maneira 1 de executar
    #Primeiro percorrer as chaves e depois os valores
    """
    for c in dicionario.keys():
        if not c in ListaSemRepeticao: #se o valor da chave nao estiver na lista
            ListaSemRepeticao.append(c) #adicionar o valor da chave na lista
            
    for v in dicionario.values():
        if not v in ListaSemRepeticao: #se o valor não estiver na lista
            ListaSemRepeticao.append(v) #adicionar o valor na lista
    """
    
    #Maneira 2 de executar
    #Percorrendo chave e seu valor ao mesmo tempo
    for c,v in dicionario.items():
        if not c in ListaSemRepeticao: #se o valor da chave nao estiver na lista
            ListaSemRepeticao.append(c) #adicionar o valor da chave na lista
        if not v in ListaSemRepeticao: #se o valor não estiver na lista
            ListaSemRepeticao.append(v) #adicionar o valor na lista
    
    return ListaSemRepeticao #retorna a lista sem itens repetidos do dicionario 