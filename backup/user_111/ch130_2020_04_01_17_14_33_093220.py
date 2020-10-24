def monta_mala(p):
    num=len(p)
    i=0
    soma=0
    nova_lista=[]
    while i<num:
        nova_lista.append(p[i])
        soma+=nova_lista[i]
        if soma>23:
            return nova_lista
        elif soma==23:
            return nova_lista
        i+=1
    if soma<23:
        return nova_lista