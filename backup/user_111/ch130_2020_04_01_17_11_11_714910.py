def monta_mala(p):
    num=len(p)
    i=0
    soma=0
    nova_lista=[]
    while i<num:
        soma+=p[i]
        if soma>23:
            return nova_lista
        nova_lista.append(p[i])
        if soma==23:
            return nova_lista
        i+=1