fibonas = []

def fib(n):
    
    if n <= 1:
        return n
    
    else:
        return(fib(n-1) + fib(n-2))

def calcula_fibonacci(n):

    for num in  range (1, n+1):

        fibonas.append(fib(num))

    return(fibonas)


print(calcula_fibonacci(10))
