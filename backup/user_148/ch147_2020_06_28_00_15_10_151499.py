def mais_frequente(palavras):
    dic = {}
    lista = []
    i = 0
    while i<len(palavras):
        lista.append(palavras.count(palavras[i]))
        dic[palavras[i]] = lista[i]
        i += 1
    
    freq = 0
    for p in dic:
        if dic[p] > freq:
            freq = dic[p]
    return p
