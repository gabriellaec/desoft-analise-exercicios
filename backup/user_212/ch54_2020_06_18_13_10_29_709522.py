def calcula_fibonacci(n):
    F = []*n
    c1 = 1
    c2 = 1
    if n == 0 :
        F=[]
    elif n == 1 :
        F[0] = c1
    elif n == 2: 
        F[0] = (c1)
        F[1] = (c2)
    else:
        F[0] = (c1)
        F[1] = (c2)
        i = 2 
        while i <= (n-2):
            F[i] = F[i-1] + F[i-2]
            i += 1
    return F