def calcula_fibonacci(x):
    lista = [0]*x
    lista[0] = 1
    lista[1] = 1
    i=2
    j = x+1
    while i<j:
        lista[i] = lista[i-1]+lista[i-2]    
        i+=1
    return lista