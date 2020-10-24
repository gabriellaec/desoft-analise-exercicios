def inverte_dicionario(dic):
    dic_novo = {}
    lista_idade = []
    for e in dic:
        i = dic[e]
        lista_idade.append(e)
        if i not in dic_novo:
            dic_novo[i] = lista_idade[e]
        else:
            dic_novo[i] += lista_idade[e]
    return dic_novo