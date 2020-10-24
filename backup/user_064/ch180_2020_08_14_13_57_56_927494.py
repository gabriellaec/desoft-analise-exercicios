def ocorrencias_letras(s):
    dicionario = {}
    for c in s:
        if c not in dicionario:
            dicionario[c] = 0
            print(dicionario)
        else:
            dicionario[c] = dicionario[c]+1
            print(dicionario)
    return dicionario