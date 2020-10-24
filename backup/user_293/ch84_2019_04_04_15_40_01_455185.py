def inverte_dicionario(dic):
    newdic = {}
    idades = []
    nomes = []
    for v in dic.values():
        if v not in idades:
            idades.append(v)
    for k in dic:
        nomes.append(k)
    for i in idades:
        for n in nomes:
            if dic[n]==i:
                if newdic[i] != []:
                    newdic[i]=[n]
                else:
                    newdic[i].append(n)
    return newdic
        