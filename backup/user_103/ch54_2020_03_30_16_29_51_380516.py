def calcula_fibonacci(n):
    F=[0]*n
    F[1]=1
    F[2]=1
    i=3
    Fibonacci=[1,1]
    while i<=n:
        F[i]=F[i-1]+F[i-2]
        i+=1
        Fibonacci.append(F[i])
    return all_num 