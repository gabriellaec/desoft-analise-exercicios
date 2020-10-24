def calcula_fibonacci(n):
    fibonacci=[1]*n
    i=2
    while i<n:
        fibonacci[i]=fibonacci[i-1]+fibonacci[i-2]
        i+=1
    return fibonacci