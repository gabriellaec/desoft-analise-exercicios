def inverte_dicionario(dic):
    invdict = {}
    for nome, idade in dic.items():
        if idade not in invdict:
        	invdict[idade] = nome
        else:
            novo = [invdict[idade]]
            novo.append(nome)
            invdict[idade] = novo
    return invdict