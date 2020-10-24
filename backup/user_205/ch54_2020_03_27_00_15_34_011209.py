def calcula_fibonacci(n):
    lista=[0]*n
    lista[0]=1
    lista[1]=1
    i = 0 
    while i<n:
        lista[i+2] = lista[i+1] + lista[i]
        i+=1
    return lista
        