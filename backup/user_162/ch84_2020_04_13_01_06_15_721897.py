def inverte_dicionario(d):
    nomes = {}
    for n, i in d.items():
        if i not in nomes:
            nomes[i] = []
        nomes[i].append(n)
    return nomes
    