def acha_bigramas(palavra):
    i = 1
    big = []
    while i<len(palavra):
        big.append(palavra[i-1]+palavra[i])
        i+=1
    return big
        
        