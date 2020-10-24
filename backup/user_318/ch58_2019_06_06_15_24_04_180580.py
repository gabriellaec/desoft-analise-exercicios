def calcula_fibonacci(n):
    lista=[]
    fibo=[1,1]
    i=0
    while i<=n-1:
        fibo.append(fibo[i]+fibo[i+1])
        lista.append(fibo[i])
        i+=1
    if n==1:
        lista.append(fibo[0])
    return lista
    
        
        
        
        