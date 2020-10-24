def calcula_fibonacci(n):
    F=[0]*n
    F[0]=1
    F[1]=1
    i=2
    while i<len(F):
        F[i]=F[i-1]+F[i-2]
        F.append(F[i])
        i+=1
    return F    
        