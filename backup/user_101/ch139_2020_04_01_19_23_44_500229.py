def listaImpar(limite):
    num = 1
    listaImpar = []
    while len(listaImpar) < limite:
        listaImpar.append(num)
        num += 2
    return listaImpar

def arcotangente(x, n):
    listaI = listaImpar(n)
    del listaI[0]
    i = 0
    arc_t = x
    while (listaI[i]//2) < n:
        arc_t -= (x ** listaI[i]) / listaI[i]
        i += 1
    return arc_t