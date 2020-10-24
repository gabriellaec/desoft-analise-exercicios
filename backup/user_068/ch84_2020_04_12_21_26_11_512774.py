def inverte_dicionario(a):
    dicionario = {}
    for p, n in a.items():
        dicionario[n] = p
    return dicionario
print(dicionario)