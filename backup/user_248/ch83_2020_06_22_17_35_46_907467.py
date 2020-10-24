def medias_por_inicial(nomes):
    inicial={}
    a={}
    for i in nomes:
        if i[0] not in inicial:
            inicial[i[0]] = nomes[i]
            a[i[0]]=1
        else: 
            inicial[i[0]] += nomes[i]
            a[i[0]] +=1
    for x in inicial:
        inicial[x] = inicial[x]/a[x]
    return inicial