def filtra_positivos(listai):
    i=0
    listan=[]
    x=len(listai)-1
    while i<x:
        if listai[i]>0:
            listan.append(listai[i])
    i+=1
    return listan