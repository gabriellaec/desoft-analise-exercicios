def monta_mala(pesagem):
    resultado=[]
    w=0
    for i in range (len(pesagem)):
        w+=pesagem[i]
        if w>23:
            break
        resultado.append(pesagem[i])
    return resultado

