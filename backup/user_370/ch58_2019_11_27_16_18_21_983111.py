def calcula_fibonacci(n):
    if n == 1:
        return 1
    elif n == 2:
        return [1,1]
    else:
    	lista, i = [1,1], 2
        while i <= n:
            lista[i+2] = lista[i] + lista[i+1]
            i -=1
        return lista