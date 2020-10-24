def calcula_fibonacci(n):
    f = [0]*n
    f[0]==1
    f[1]==1
    if n==0:
        return []
    if n == 1:
        return [1]
    if n == 2:
        return [1,1]
    else:
        i=1
        while i<=n:
            i+=1
            f[i] = f[i-1] + f[i-2]
        return f