def inverte_dicionario(dic_inicial):
    dic_invert={}
    for nome in dic_inicial:
        if dic_inicial[nome] in dic_invert:  
            dic_invert[dic_inicial[nome]]=[dic_invert[dic_inicial[nome]]]
            dic_invert[dic_inicial[nome]].append(nome)
        else:
            dic_invert[dic_inicial[nome]]=nome
    
    return dic_invert