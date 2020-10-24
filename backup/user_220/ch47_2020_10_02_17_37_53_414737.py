def estritamente_crescente(lista):
    novalista = []
    t=0
    while t<len(lista):
        if lista[t] >= lista[t+1]:
            t+=1
        else:
            novalista.append(lista[t])
            t+=1
    return novalista