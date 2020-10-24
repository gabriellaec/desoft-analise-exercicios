def calcula_fibonacci(n):
    lista=[0]*n
    if n==1:
        return [1]
    elif n==2:
        return[1,1]
    else: 
        for i in range(2,n-1):
            lista[0]=1
            lista[1]=1
            lista.append(lista[i-1]+lista[i-2])
    return lista