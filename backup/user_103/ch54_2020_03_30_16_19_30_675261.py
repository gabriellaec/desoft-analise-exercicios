def calcula_fibonacci(n):
    i=3
    F[i]=F[i-1]+F[i-2]
    F[1]=1
    F[2]=1
    all_num=[1,1]
    while i<n :
        F[i]=F[i-1]+F[i-2]
        i+=1
        all_num.append(F[i])
    return all_num 