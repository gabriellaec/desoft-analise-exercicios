def inverte_dicionario(dic):
    new = {}
    for n,i in dic.items():
        if i not in new:
            new[i] = [n]
        else:
            new[i].append(n)
    return new