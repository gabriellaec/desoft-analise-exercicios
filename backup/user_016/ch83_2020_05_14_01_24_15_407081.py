def inicial(dicionario1):
    dicionario2 = {}
    for u in dicionario1.keys():
        if u[0] not in dicionario2.keys():
            lista = []
            for i in dicionario1.keys():
                if i[0] == u[0]:
                    lista.append(dicionario1[i])
            dicionario2[u[0]] = sum(lista)/(len(lista))
    return dicionario2
     
            