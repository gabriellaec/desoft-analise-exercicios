def calcula_fibonacci(n):
    nzero=1
    num=1
    i = 2
    f(n) = f (n-1)+ f(n-2)
    f[2] = nzero+num
    soma = [] 
    while i <=n-1:
        f[i] = f[i-1] + f[i-2]
        i+=1
        soma.append(f[i])
    return soma
        
    