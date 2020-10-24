def calcula_fibonacci(n):
    fibonacci=[0]*n
    fibonacci[0]=1
    fibonacci[1]=1
    i=2
    while i<n:
        fibonacci[n]=fibonacci[n-1]+fibonacci[n-2]
        i+=1
    return fibonacci
    