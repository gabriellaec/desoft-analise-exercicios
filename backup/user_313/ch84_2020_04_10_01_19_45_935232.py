def inverte_dicionario (d1):

    saida = {}
    values = {}
    nomes = []
    Cont = 0
    for k, v in d1.items():
        nomes.append(k)
        if v not in saida:
            a = [k]
            saida[v] = a
        else:
            a = [k]
            saida[v] = saida[v] + a

    return saida