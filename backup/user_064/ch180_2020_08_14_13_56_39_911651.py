def ocorrencias_letras(s):
    dicionario = {}
    for c in s:
        if c not in dicionario:
            dicionario[c] = 0
        else:
            dicionario[c] += 1
    return dicionario