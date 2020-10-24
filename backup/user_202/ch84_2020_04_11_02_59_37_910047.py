def inverte_dicionario(pessoas):
    dic = {}
    for k,v in pessoas.items():
        if v not in dic:
            dic[v] = 'n'
    nomes = []
    for i in dic:
        for k,v in pessoas.items():
            if v == i:
                nomes.append(k)
        dic[i] = nomes
        nomes.clear()
    return dic
        