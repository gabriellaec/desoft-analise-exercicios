def monta_mala(l):
    p=[]
    i=0
    while i<len(l):
        if l[i]<=23:
            p.append(l[i])
            if sum(p)>23:
                del p[i]
                return(p)
                break
            else:
                i+=1
        else:
            i+=1
    return(p)