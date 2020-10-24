def verifica_progressao(lista):
    
    if len(lista)>2:
    
        i = 0
        PA = True
        PG = True 
        while i < len(lista) - 2:
            if not lista[i + 1] - lista[i] == lista[2+i] - lista[i+1]:
                PA= False

            if not lista[i+1]/lista[i] == lista[2+i]/lista[1+i]:
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
    else:
        return "NA"