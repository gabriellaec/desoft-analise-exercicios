def estritamente_crescente(lista):
    novalista = []
    novalista.append(lista[0])
    x = max(novalista)
    t=1
    while t<len(lista):
        if x >= lista[t]:
            t+=1
        else:
            novalista.append(lista[t])
            x = max(novalista)
            t+=1
    return novalista