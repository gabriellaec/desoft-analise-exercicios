l1=[]
def monta_mala(l):
    t=0
    i=0
    while t<23:
        t=t+l[i]
        l1.append(l[i])
        i+=1
    if t>23:
        del(l1[i-1])
    return l1
