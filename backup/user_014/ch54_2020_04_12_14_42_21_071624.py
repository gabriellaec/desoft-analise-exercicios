def calcula_fibonacci (n):
    F[n] = F[n-1] + F[n-2]
    F[1] = 1
    F[2] = 1
    for i in n:
        F[i]= F [i-1] + F[i-2]
    return F.append(F[n])