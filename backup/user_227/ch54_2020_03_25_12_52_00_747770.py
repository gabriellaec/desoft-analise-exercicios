def calcula_fibonacci(n):
    F=[0]*n
    F[0] = 1
    F[1] = 1
    i = 2
    while i < n:
        F[i] = F[i] + F[i-1]
        i += 1
     
    return F