def acha_bigramas(palavra):
    bigramas=[]
    i=0
    while i< len(palavra)-1:
        if not palavra[i:i+2] in bigramas:
            bigramas.append(palavra[i:i+2])  
        i+=1
    return bigramas