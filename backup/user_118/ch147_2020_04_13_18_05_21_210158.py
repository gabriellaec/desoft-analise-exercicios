def mais_frequente(l):
    dicionario = {}
    o = 0
    for i in l:
        if i in dicionario:
            dicionario[i] += 1
        else:
            dicionario[i] = 1
    palavra = ''
    for e in dicionario.keys():
        if dicionario[e] > o:
            o = dicionario[e]
            palavra = e
    return palavra