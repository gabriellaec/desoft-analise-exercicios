def conta_bigramas(string):
    dicionario = {}
    i = 0
    while i < len(string) - 1:
        if not (string[i]+string[i+1]) in dicionario:
            dicionario[string[i]+string[i+1]] = 1
        else:
            dicionario[string[i]+string[i+1]] += 1
        i += 1
    return dicionario