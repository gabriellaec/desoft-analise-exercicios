def acha_bigramas(palavra):
    lista = []
    for i in range(len(palavra)-1):
        big = palavra[i:i+2]
        if big not in lista:
            lista.append(big)
    
    return lista

print(acha_bigramas("babador"))