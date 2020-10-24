
def arcotangente(x,n):
    contador=0
    m = 3
    i = 3
    u = -1
    z = x
    while (contador<n):
        z += u*(x**m/i)
        u*=-1
        m+=2
        i+=2
        contador+=1
    return z