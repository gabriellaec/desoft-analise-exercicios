def  conta_letras(a):
    dicionario = {}
    for c in a:
        if c in dicionario.keys():
            dicionario[c] += 1
        else:
            dicionario[c] = 1
    return dicionario