def acha_bigramas(palavra):
    bigramas=[]
    for i in range(len(palavra)-1):
        if palavra[i:i+2] not in bigramas:
            bigramas.append(palavra[i:i+2])  
    return bigramas
print(acha_bigramas("banana"))
