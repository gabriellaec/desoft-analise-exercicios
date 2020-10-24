def verifica_progressao(x):
    listapa=[x[0],x[1]]
    listapg=[x[0],x[1]]
    i=1
    a=(x[1]-x[0])
    g=(x[1]/x[0])
    while len(listapa)<=len(x):
        listapa.append(listapa[i]+a)
        i+=1
    i=1
    while len(listapg)<=len(x):
        listapg.append(listapg[i]*g)
    if listapa==listapg and listapa==x:
        return "AG"
    elif listapa==x and listapa!=listapg:
        return "PA"
    elif listapg==x and listapg!=listapa:
        return "PG"
    else:
        return "NA"