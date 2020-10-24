def monta_mala(p):
    num=len(p)
    i=0
    soma=0
    while i<num:
        soma+=p[i]
        if soma>23:
            del p[i]
            return p
        i+=1