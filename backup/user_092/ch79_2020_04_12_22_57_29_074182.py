def monta_dicionario(x):
    dicionario={}
    i = 0
    for elemento in x:
        chave = elemento[i]
        valores = elemento[i+1]
        dicionario[valores] = chave
        i += 1
    return dicionario