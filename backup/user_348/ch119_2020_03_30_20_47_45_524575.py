def fatorial(n):
    r = 1
    contador = 1
    while c<= n:
        r = r*contador
    return r
def calcula_euler(x,n):
    i = 1
    e = 1
    while i<n:
        e = e+(x**i)/fatorial(i)
        i = i+1
    return e
    

        