def monta_mala(l):
    p=[]
    for i in range (0,len(l)):
        if sum(p)+l[i]<=23:
            p.append(l[i])
        else:
            return(p)