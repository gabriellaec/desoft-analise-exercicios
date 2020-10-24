def monta_mala(l):
    p=[]
    i=0
    while i<len(l):
        if sum(p)+l[i]<=23:
            p.append(l[i])
            i+=1
        else:
            return(p)