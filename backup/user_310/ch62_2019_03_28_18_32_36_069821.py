def filtra_positivos(l):
    nova_l=[]
    
    i=0
    
    while i<len(l):
        if l[i]>0:
            nova_l.append(l[i])
        i+=1
    return nova_l