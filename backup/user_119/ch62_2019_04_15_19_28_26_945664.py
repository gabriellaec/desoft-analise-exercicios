def filtra_positivos(listai):
    i=0
    listan=[]
    while i<(len(listai)-1):
        if listai[i]>0:
            listan.append(listai[i])
    i+=1
    return listan