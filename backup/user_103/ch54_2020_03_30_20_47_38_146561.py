def calcula_fibonacci(n):  
    if n==1 or n==2:
        return 1
    F=[0]*n
    F[1]=1
    F[2]=1
    i=3
    while i<=n:
        F[i]=F[i-1]+F[i-2]
        i+=1
    return F
