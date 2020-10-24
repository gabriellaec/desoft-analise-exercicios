
def arcotangente(x,n):
    m = 3
    i = 3
    u = -1
    z = x
    while (m<n):
        z += u*(x**m/i)
        u*=-1
        m+=2
        i+=2
    return z
   