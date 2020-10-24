def acha_bigramas(palavra):
    i = 1
    big = []
    while i<len(palavra):
        bigrama = palavra[i-1]+palavra[i]
        if bigrama not in big:
            big.append(bigrama)
            i+=1
        else:
            i+=1
    return big
        
        