def verifica_progressao(lista):
    PA = True 
    PG = True
    i = 0
    while i+2 < len(lista):
        if lista[i+1]-lista[i] != lista[i+2]-lista[i+1]:
            PA = False
            break
    while i+2 < len(lista):
        if lista[i+1]/lista[i] != lista[i+2]/lista[i+1]:
            PG = False
            break
        if PA == True and PG == False:
            return "PA"
        if PA == False and PG == True:
            return "PG"
        if PA == True and PG == True:
            return "AG"
        if PA == False and PG == False:
            return "NA"
