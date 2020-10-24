def monta_mala(pesagem):
    pesos=[]
    w=0
    for i in range (len(pesagem)):
        w+=pesagem[i]
        if w>23:
            break
        pesos.append(pesagem[i])
    return resultado

