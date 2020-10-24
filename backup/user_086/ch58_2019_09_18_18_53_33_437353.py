def calcula_fibonacci(n):
    contador=
    f=[]
    if n==0:
        return f
    if n==1:
        f.append(1)
    f[1]=1
    while contador<=n:
        f[contador]=f[contador-2]+f[contador-1]
        contador+=1
    return f