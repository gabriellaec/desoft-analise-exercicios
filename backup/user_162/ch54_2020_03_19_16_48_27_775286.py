def calcula_fibonacci(n):
    lis= [1, 1]
    i=0
    while i!=n:
        lis.append(lis[-1] + lis[i])
        i+=1
    return lis