def verifica_progressao(lista):
    PA = True
    PG = True 
    for i in lista: 
        if lista[i+2] != (lista[i]+lista[i+1])/2:
            PA = False
        if lista[i+1]**2!=lista[i]*lista[i+2]:
            PG = False
if PA:
    return "PA"
elif PG:
    return "PG"
elif PA and PG:
    return "AG"
else:
    return "NA"

        
        
        