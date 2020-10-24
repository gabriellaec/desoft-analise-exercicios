def conta_bigramas(palavra):
    bigrama = {}
    for i in range(len(palavra)):
        if (i == len(palavra)-1):
            break
        
        else:
            bigrama_1 = palavra[i] + palavra[i+1]
            if bigrama_1 in bigrama:
                bigrama[bigrama_1] +=1 
                
            else:
                bigrama[bigrama_1]= 1
    return bigrama