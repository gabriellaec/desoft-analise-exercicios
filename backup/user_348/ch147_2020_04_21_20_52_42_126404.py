def mais_frequente (palavras):
    dicionario = {}
    i = 0
    for i in palavras:
        if not i in dicionario:
            dicionario[i] = 1
        else: 
            dicionario[i] = dicionario[i] + 1
    c = 0
    for j in dicionario:
        if dicionario[j] > c:
            c = dicionario[j]
            palavra_frequente = j
    return palavra_frequente
    