l1=[]
def monta_mala(l):
    t=0
    i=(-1)
    while t<23 and t!=23:
        i+=1
        t=t+l[i]
        l1.append(l[i])
    if t>23:
        del(l1[i])
    return l1
