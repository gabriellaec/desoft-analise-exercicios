def filtra_positivos(n):
    positivos=[]
    i=0
    while i<len(n):
        if n[i]>0:
            positivos.append(n[i])
        i+=1
    return positivos