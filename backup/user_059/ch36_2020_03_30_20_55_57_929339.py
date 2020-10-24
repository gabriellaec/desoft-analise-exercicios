def fatorial(x):
    i = 1
    soma = 1
    while i<x:
        soma = soma*i*(i+1)
        i+=1
    return soma