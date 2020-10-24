def inverte_dicionario(n):
    dict = {}
    for i, e in n.items():
        if e not in dict:
            dict[e] = [i]
        else:
            dict[e].append(i)
    return dict