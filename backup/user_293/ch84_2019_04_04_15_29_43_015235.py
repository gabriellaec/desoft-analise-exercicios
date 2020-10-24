def inverte_dicionario(dic):
    nomes = dic.keys()
    idades = dic.values()
    newdic = {idades[i]:nomes[i] for i in range(len(nomes))}
    return newdic
        