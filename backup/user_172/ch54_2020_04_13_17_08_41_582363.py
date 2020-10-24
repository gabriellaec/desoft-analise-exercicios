def calcula_fibonacci(n):
    lista = []
    n = len(lista)
    if n == 1:
        lista = [1]
    elif n == 2:
        lista = [1,1]
    i = 2
    
    while n>i:
        lista[i] = lista[i-1] + lista[i-2]
        i+=1
    return lista  