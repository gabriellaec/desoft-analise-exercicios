def calcula_fibonacci(n):
    lista=[0]*n
    lista[0]=1
    if n==1:
        return lista
    else:
        lista[1]=1
        n==len(lista)-1
        i=0
        for i in lista:
            lista[i]=lista[i-1]+lista[i-2]
            lista.append(i)
            i+=1
            return lista
        
    
    