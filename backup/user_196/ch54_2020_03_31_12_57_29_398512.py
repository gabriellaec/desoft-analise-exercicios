def calcula_fibonacci(n):
    F = [] * n
    F [0] = 1
    F [1] = 1
    i=2
    while (i<n):
        F[i]= F[i-1] + F[i-2]
        i+=1
    return (F)