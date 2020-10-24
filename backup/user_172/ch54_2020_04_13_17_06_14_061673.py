def calcula_fibonacci(n):
    lista = [1,1]
    i = 2
    n = len(lista)
    while n>i:
        lista[i] = lista[i-1] + lista[i-2]
        i+=1
    return lista  