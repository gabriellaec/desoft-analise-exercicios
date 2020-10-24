def calcula_fibonacci(n):
    lista=[]
    fibo=[1,1]
    i=0
    while i<n-2:
        a=fibo[i]+fibo[i+1]
        lista.append(a)
        i+=1
    if n==1:
        del(lista[1])
    return lista
    
        
        
        
        