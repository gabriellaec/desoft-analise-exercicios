def inverte_dicionario(dic):
    newdic = {}
    nomes = []
    idades = []
    for k, v in dic.items():
        nomes.append(k)
        if v not in idades:
            idades.append(v)
    for i in idades:
        newdic[i] = []
        for n in nomes:
            if dic[n] == i:
                newdic[i].append(n)
    return newdic
        
    
        