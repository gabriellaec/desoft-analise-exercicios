def calcula_fibonacci(n):
    contador=2
    f=[]
    if n==0:
        return f
    if n==1:
        f.append(1)
        return f
    f.append(1)
    f.append(1)
    while contador<n:
        novovalor=f[contador-2]+f[contador-1]
        f.append(novovalor)
        contador+=1
    return f
[1:19 p.m., 2019-11-27] Desa: 66