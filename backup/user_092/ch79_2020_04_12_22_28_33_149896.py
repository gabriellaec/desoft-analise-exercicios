def monta_dicionario(x):
    dicionario={}
    for elemento in x:
        chave = elemento[0]
        valores = elemento[1]
        dicionario[valores] = chave
    return dicionario