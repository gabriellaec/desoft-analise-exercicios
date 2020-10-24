def verifica_progressao(lista):
    for i in range(0,len(lista)):
        while lista[i+1]-lista[i] = lista[i+2]-lista[i+1]:
            PA = True
            i+=1
        while lista[i+1]/lista[i] = lista[i+2]/lista[i+1]:
            PG = True
            i+=1
        if PA = True and PG != True:
            return "PA"
        if PA != True and PG = True:
            return "PG"
        if PA = True and PG = True:
            return "AG"
        if PA != True and PG != True:
            return "NA"
