def acha_bigramas (palavra):
    lista=[]
    i=0
    while i<(len(palavra)-1):
        bigrama= palavra[i]+palavra[i+1]
        if bigrama not in lista:
            lista.append(bigrama)
        i=i+1
    return bigrama
            
        