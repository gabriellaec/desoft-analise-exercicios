def fatorial(n):
    r = 1
    contador = 1
    while contador<= n:
        r = r*contador
        contador = contador + 1
    return r
def calcula_euler(x,n):
    i = 1
    e = 1
    while i<n:
        e = e+(x**i)/fatorial(i)
        i = i+1
    return e
    

        