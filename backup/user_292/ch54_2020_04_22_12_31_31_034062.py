def calcula_fibonacci(n):
    F = [1,1]
    if n == 1:
        return F[0]
    for i in range(0,n-2):
        F.append(F[i+1]+F[i])
    return F