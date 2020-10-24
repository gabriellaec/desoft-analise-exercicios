def verifica_progressao(lista):
    
    if len(lista)>2:
    
        i = 0
        PA = True
        PG = True 
        while i < len(lista) - 2:
            if not lista[i+1]*2 == lista[i] + lista[i+2]:
                PA= False

            if not lista[i+1]**2 == lista[i]*lista[i+2]:
                PG = False
            i+=1

        if PA == True and PG == True:
            return "AG"
        elif PA == True and PG == False:
            return "PA"
       	elif PA == False and PG == True:
            return "PG"
        else:
            return "NA"
    elif len(lista) == 2:
        return "AG"
    else:
        return "NA"