def calcula_fibonacci(n):
    lista=[0]*n
    if n==1:
        return [1]
    elif n==2:
        return[1,1]
    else: 
        i=2
        lista[0]=1
        lista[1]=1
        while(i<n):
            lista[i]=lista[i-1]+lista[i-2]
            i+=1
        return lista