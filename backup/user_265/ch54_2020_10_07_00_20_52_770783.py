def calcula_fibonacci(n):
    F = [1, 1]
    i = 0
    while i < n-2:
        prox = F[i] + F[i+1]
        F.append(prox)
        i += 1
        
    return F