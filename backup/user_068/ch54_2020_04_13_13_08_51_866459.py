def calcula_fibonacci(n):
    i = 2
    F = [1, 1]
    while i < n:
        F[i] = F[i-1] + F[i-2]
        F.append(F[i])
        i += 1
    if n == 1:
        return [1]
    return F
