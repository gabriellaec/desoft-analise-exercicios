def primeiras_ocorrencias(string):
    dic= {}
    listacarac= []
    palavra=[]
    for i in range(len(string)):
        if string[i] not in listacarac:
            listacarac.append(string[i])
            palavra.append(i)
    for indice in range(len(listacarac)):
        dic[listacarac[indice]]= palavra[indice]
    return dic
