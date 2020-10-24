def inverte_dicionario(dic):
    q = {}
    for n,i in dic.items():
        if i not in q:
            q[i] = [n]
        else:
            q[i] = q[i] + [n]
    return q