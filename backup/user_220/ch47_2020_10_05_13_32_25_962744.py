lista = [10, 15, 11, 12, 13, 14]

def estritamente_crescente(lista):
    novalista = []
    novalista.append(lista[0])
    t=0
    x = max(lista)
    while t<len(lista):
        if x >= lista[t]:
            t+=1
        else:
            novalista.append(lista[t])
            t+=1
    return novalista

