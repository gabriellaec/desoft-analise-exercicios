def calcula_fibonacci(n):
    lista = [1,1]
    for i in range(n):
        lista[i+2] = lista[i+1] + lista[i]
    return lista

