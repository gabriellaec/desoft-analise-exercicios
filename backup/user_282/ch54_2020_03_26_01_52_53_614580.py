def calcula_fibonacci(n):  
    Fibonacci = [0]*n
    Fibonacci[0] = 1
    Fibonacci[1] = 1
    i = 2
    while (i<n):
       Fibonacci[i] = Fibonacci[i-1] + Fibonacci[i-2]
       i += 1
    return(Fibonacci)