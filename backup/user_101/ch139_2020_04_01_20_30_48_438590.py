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
    while i < (len(listaI)-1):
        arc_t -= (x ** listaI[i]) / listaI[i]
    
    return arc_t