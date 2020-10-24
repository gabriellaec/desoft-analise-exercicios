def filtra_positivos(numerosreais):
    i=0
    estrposit=[]
    while i<len(numerosreais):
        if numerosreais[i]>0:
            estrposit.append(numerosreais[i])
        i+=1
    return estrposit