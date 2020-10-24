def monta_mala(l):
    p=[]
    i=0
    while i<len(l):
        if l[i]<=23:
            p.append(l[i])
            i+=1
        else:
            return(p)