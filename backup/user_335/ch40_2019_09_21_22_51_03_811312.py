def fatorial(n):
    valor = 1
    if n == 0:
        return 0
    else:    
        while n!=1:
            valor *= n
            n = n-1
    return valor