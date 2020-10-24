def calcula_fibonacci(n):
    f=[0 for i in range(n)]
    f[0]=1
    f[1]=1
    
    i=2
    
    while(i<n):
        f[i]=f[i-1]+f[i-2]
        i+=1
    
    return f