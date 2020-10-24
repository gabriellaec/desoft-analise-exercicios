def acha_bigramas(palavra):
    bigrama=[]
    
    i=1
    
    while i<len(palavra):
        bg= palavra[i-1]+palavra[i]
        if bg not in bigrama:
            bigrama.append(bg)
        i+=1
    return bigrama

print(acha_bigramas('babador'))