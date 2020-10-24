def filtra_positivos(lista):
    ln=[]
    i=0
    while i<len(lista):
        if lista[i]>0:
            ln.append(lista[i])
        else:
            pass
        i+=1
    return ln   
