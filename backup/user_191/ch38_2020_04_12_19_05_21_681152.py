def quantos_uns(n):
    soma=[]
    u=str(n)
    for i in range(len(u)):
        if i=='1':
            soma.append(1)
    return sum(soma)