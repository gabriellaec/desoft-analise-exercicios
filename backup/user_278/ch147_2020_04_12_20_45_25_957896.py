def mais_frequente (palavras):
    freq_dic = {}
    for i in palavras:
        if i not in freq_dic:
            freq_dic[i] = 1
        else:
            freq_dic[i] += 1
    palavras = list(freq_dic.keys())
    lista1 = list(freq_dic.values())
    return palavras[lista1.index(max(lista1))]