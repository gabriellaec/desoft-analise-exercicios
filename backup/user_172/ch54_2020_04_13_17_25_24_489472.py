def calcula_fibonacci(n):
    lista = []
    i = 0
    x = lista[i]
    n = len(lista)
    if i == 0 or i == 1:
        x == 1
    elif i>=2:
        while n>i:
            lista [i] = lista[i-1]+lista[i-2]
    print (lista)        
    return lista