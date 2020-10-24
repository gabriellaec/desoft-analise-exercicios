def verifica_progressao(lista):
    PA = True
    PG = True 
    for i in range(len(lista)-2): 
        if lista[i+2] != (lista[i]+lista[i+1])/2:
            PA = False
        if lista[i+1]**2!=lista[i]*lista[i+2]:
            PG = False
    if PA:
        return "PA"
    elif PG:
        return "PG"
    elif not PA and PG:
        return "NA"
    else:
        return "AG"
            


        
        
        
