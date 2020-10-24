def calcula_fibonacci(n):
    lista=[0]*n
    lista[0]=1
    if n==1:
        return lista
    elif n==2:
        lista[1]=1
        return lista
    i=0
    while n>=3:
        lista[i]=lista[i-1]+lista[i-2]
        lista.append(i)
        i+=1
        return lista
        
    
    