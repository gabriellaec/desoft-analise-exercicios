def filtra_positivos (x):
    l=[]
    i=0
    while i < len (x):
        if x[i]>0:
            i+=1
            l.append(x[i])
    return l
            
        