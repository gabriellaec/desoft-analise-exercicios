def mais_frequente(palavras):
    dic = {}
    lista = []
    i = 0
    while i<len(palavras):
        lista.append(palavras.count(palavras[i]))
        dic[palavras[i]] = lista[i]
        i += 1
    for k, v in dic.items():
        if v == max(lista):
            return k