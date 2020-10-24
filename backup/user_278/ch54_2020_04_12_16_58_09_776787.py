def calcula_fibonacci (n):
    F = [0]*n
    if n==0:
        return []
    elif n==1:
        F[0] = 1
        return F
    elif n==2:
        F[0] = 1
        F[1] = 1
        return F
    F[0] = 1
    F[1] = 1
    for i in range (0,len(F)-2):
        F [i+2] = F[i+1] + F[i]
    return F