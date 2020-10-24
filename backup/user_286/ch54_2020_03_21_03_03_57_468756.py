def calcula_fibonacci(n):
    if n == 1:
        return [1]
    elif n == 2:
        return [1,1]
    else: 
        lista_fib = [1,1]
        while len(lista_fib) != n:
            lista_fib.append(lista_fib[-1] + lista_fib[-2])
        
        return lista_fib
