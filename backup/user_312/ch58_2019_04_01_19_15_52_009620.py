def calcula_fibonacci(n):
    z=1
    lista=[1]
    x=1
    w = 0
    while w<n-1:
        p=x #armazena ultimo valor
        x=x+z #soma proximo valor
        z=p #transfere ultimo valor
        w=w+1 #incrementa contador
        lista.append(p)
    return lista
print(calcula_fibonacci(2))