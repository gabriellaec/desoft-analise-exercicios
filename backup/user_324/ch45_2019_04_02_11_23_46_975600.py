def zera_negativos(l):
    i=0
    zera_negativo=[]
    for e in l:
        if l[i]<0:
            l[i]=0
            zera_negativo.append(l[i])
        elif l[i]>0:
            zera_negativo.append(l[i])
        elif l[i]==0:
            zera_negativo.append(l[i])
        i+=1
    return zera_negativo
       
            
            