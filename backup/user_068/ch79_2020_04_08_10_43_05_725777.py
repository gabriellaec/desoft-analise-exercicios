def monta_dicionario(a, b):
    dicionario = {}
    for i in range(len(a)):
        dicionario[a[i]] = [b[i]]
    return dicionario