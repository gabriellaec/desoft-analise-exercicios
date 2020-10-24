def acha_bigramas(palavra):
    l_bi = []
    i = 0
    while i < len(palavra) - 1:
        bi = palavra[i] + palavra[i+1]
        l_bi.append(bi)
        i+=1
    return l_bi