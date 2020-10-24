def calcula_fibonacci(n):
    F=[0]*n
    F[0] = 1
    i = 1
    while i < n:
        if i == 1:
            F[1] = 1
        else:
            F[i] = F[i-1] + F[i-2]
            i += 1
     
    return F

