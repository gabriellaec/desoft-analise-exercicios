def acha_bigramas(palavra):
    i = 0
    big = []
    while i<len(palavra):
        bigrama = palavra[i]+palavra[i+1]
        if bigrama not in big:
            big.append(bigrama)
            i+=1
        else:
            i+=1
    return big
        
        