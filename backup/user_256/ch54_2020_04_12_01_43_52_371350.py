def calcula_fibonacci(n):
    nzero=1
    num=1
    i = 2
    soma = [] 
    while i <=n-1:
        n[i] = n[i-1] + n[i-2]
        i+=1
        soma.append(n[i])
    return soma
        
    