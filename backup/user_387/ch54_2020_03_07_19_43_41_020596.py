fibonas = []

def fib(n):
    
    if n <= 1:
        return n
    
    else:
        return(fib(n-1) + fib(n-2))

def calcula_fibonacci(n):

    for num in  range (1, n):

        fibonas.insert(num, fib(num))

    return(fibonas)
