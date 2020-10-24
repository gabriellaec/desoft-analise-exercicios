def calcula_fibonacci(a):
    lista=[1]*a
    i=2
    while i<a:
        lista[i]=lista[i-1]+lista[i-2]
        i+=1
    return lista