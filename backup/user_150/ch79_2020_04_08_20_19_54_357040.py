def monta_dicionario(key, value):
    dicionario = {}
    i = 0
    while i < len(key):
        dicionario[key[i]] = value[i]
        i += 1
    return dicionario