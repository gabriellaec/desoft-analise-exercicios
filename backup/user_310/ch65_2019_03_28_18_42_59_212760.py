def acha_bigramas(palavra):
    bigrama=[]
    
    i=1
    
    while i<len(palavra):
        bg= palavra[i-1]+palavra[i]
        bigrama.append(bg)
        i+=1
    return bigrama