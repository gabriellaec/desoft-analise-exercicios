def calcula_fibonacci(x):
    j = x+1
    lista = [0]*j
    lista[0] = 1
    lista[1] = 1
    i=2
    while i<j:
        lista[i] = lista[i-1]+lista[i-2]    
        i+=1
    return lista
