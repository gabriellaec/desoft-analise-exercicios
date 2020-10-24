def calcula_fibonacci(n):
    lista_fib = []
    lista_fib.append([1]*2)
    while len(lista_fib) != n:
        lista_fib.append(lista_fib[-1] + lista_fib[-2])
    
    return lista_fib