def fatorial(n):
    contador=1 
    n_fatorial= contador * n
    while contador< n:
        n_fatorial= n_fatorial* contador 
        contador +=1
    return n_fatorial
        