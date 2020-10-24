def listaImpar(limite):
    num = 1
    listaImpar = []
    while len(listaImpar) < limite:
        listaImpar.append(num)
        num += 2
    return listaImpar

def arcotangente(x, n):
    listaI = listaImpar(n)
    i = 0
    arc_t = 0
    while i < (len(listaI)-1):
        solucao = listaI[i]//2
        if solucao % 2 == 0:
            arc_t += ((x ** listaI[i]) / (listaI[i]))
        else:
            arc_t -= ((x ** listaI[i]) / (listaI[i]))
        i += 1
    
    return arc_t