def inverte_dicionarios(dicionario):
    dic={}
    for nome in dicionario:
        idade=dicionario[nome]
        if idade in dic:
            dic[idade].append(nome)
        else:
            dic[idade]=[nome]
            
    return dic