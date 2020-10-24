def inverte_dicionario(dicionario1):
    dicionario2 = {}
    for u in dicionario1.values():
        if u not in dicionario2.keys():
            lista = []
            for i in dicionario1.keys():
                if dicionario1[i] == u:
                    lista.append(i)
                else:
                    pass 
            dicionario2[u] = lista
        else:
            pass
    return dicionario2