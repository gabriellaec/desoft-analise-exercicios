def verifica_progressao(lista):
    print(lista)
    PA = True 
    PG = True
    i = 0
    while i+2 < len(lista):
        if lista[i+1]-lista[i] != lista[i+2]-lista[i+1]:
            PA = False
            break
        i+=1
    while i+2 < len(lista):
        if lista[i+1]/lista[i] != lista[i+2]/lista[i+1]:
            PG = False
            break
        i+=1
    if PA == True and PG == False:
        print("PA")
        return "PA"
    if PA == False and PG == True:
        print("PG")
        return "PG"
    if PA == True and PG == True:
        print("AG")
        return "AG"
    if PA == False and PG == False:
        print("NA")
        return "NA"
