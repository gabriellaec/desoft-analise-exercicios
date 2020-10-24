def filtra_positivos(list):
    n=len(list)
    i=0
    new=[]
    
    while i < n:
        if list[i] > 0:
            a=list[i]
            new.append(a)
        i=i+1
    return new