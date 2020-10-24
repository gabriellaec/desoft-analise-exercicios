def fatorial(numero):
    fatorial=1
    contador=1
    while contador!=numero+1:
        fatorial=fatorial*contador
        contador+=1
    return fatorial