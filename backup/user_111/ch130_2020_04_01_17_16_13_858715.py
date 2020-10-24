def monta_mala(p):
    num=len(p)
    i=0
    soma=0
    nova_lista=[]
    while i<num:
        soma+=p[i]
        if soma>23:
            return nova_lista
        elif soma==23:
            nova_lista.append(p[i])
            return nova_lista
        nova_lista.append(p[i])
        i+=1
    if soma<23:
        return nova_lista