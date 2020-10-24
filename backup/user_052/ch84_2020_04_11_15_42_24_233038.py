def inverte_dicionario(pessoas):
    dic = {}
    for v in pessoas.values():
        if v not in dic:
            dic[v] = 'n'
    nomes = []
    for i in dic:
        nomes.clear()
        for k,v in pessoas.items():
            if v == i:
                nomes.append(k)
        dic[i] = nomes
    return dic