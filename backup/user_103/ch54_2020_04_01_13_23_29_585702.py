def calcula_fibonacci(n):  
    if n==2:
        return [1,1]
    if n==1:
        return [1]
    F=[1,1]
    i=3
    while i<=n:
        F.append(F[i-2]+F[i-3])
        i+=1

    return F
