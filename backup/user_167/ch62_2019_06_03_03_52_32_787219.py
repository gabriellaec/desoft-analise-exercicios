def filtra_positivos (x):
    l=[]
    i=0
    while i < len (x):
        if x[i]>0:
            l.append(x[i])
            i+=1
    return l
            
        