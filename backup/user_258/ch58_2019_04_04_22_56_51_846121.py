def calcula_fibonacci(n):
    lista=[]
    fib=[]
    fib[0]=1
    fib[1]=1
    i=2
    while i<n:
        fib[i]=fib[i-1]+fib[i-2]
        lista.append(fib[i])
        i+=1
    return lista
    
    