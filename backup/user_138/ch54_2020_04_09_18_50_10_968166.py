def calcula_fibonacci(n):
    i=0
    lista=[]
    lista[0]=1
    lista[1]=1
    if n==1:
        return lista[0]
    elif n==2:
        return lista[0,1]
    while (i+2)<n:
        lista[i+2]=lista[i+1]+lista[i]
        i+=1
    return lista