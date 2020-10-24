def zera_negativos(l):
    i=0
    nova_l=[]
    while i<len(l):
        if l[i]<0:
            l[i]=0
            nova_l.append(l[i])
        else:
            nova_l.append(l[i])
        i+=1
    return nova_l