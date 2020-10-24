def acha_bigramas(palavra):
    bigramas=[]
    for i in range(len(palavra)):
        if not palavra[i:i+1] in bigramas:
            bigramas.append(palavra[i:i+1])  
    return bigramas