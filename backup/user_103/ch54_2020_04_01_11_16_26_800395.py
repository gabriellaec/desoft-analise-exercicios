def calcula_fibonacci(n):  
    if n==2:
        return [1,1]
    if n==1:
        return [1]
    F[1]=1
    F[2]=1
    F=[1,1]
    i=3
    while i<=n:
        F.append(F[i-1]+F[i-2])
        i+=1
    print (F)
