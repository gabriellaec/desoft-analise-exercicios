def filtra_positivos(l):
    l2 = []
    i = 0
    
    while i<len(l):
        if l[i]>0:
            l2.append(l[i])
        i += 1
        
    return l2
