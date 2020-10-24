def inverte_dicionario(d):
    dnovo = {}
    for i in d.values():
        if i not in dnovo.keys():
            lista = []
            for j in d.keys():
                if d[j] == i:
                    lista.append(j)
            dnovo[i] = lista
    return dnovo
    