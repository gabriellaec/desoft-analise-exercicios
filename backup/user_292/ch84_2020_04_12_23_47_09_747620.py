
def inverte_dicionario(dic):
    q = {}
    nome = []
    for n,i in dic.items():
        if i not in q:
            q[i] = n
        else:
            nome.append(q[i])
            nome.append(n)
            q[i] = nome
    return q