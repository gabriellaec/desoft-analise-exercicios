def calcula_fibonacci (n):
    F = []
    F[1] = 1
    F[2] = 1
    for i in range n:
        F[i]= F [i-1] + F[i-2]
    return F.append(F[n])