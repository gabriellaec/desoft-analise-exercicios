def acha_bigramas(palavra):
    i = 0
    big = []
    while i<len(palavra):
        big.append(palavra[i]+palavra[i+1])
        i+=2
    return big
print(acha_bigramas('babador'))
        
        