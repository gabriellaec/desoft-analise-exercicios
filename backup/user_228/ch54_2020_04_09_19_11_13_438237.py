def calcula_fibonacci(n):
    f=[0]*n
    f[0]=1
    f[1]=1
    i=1
    while i<n-1:
        f[i+1]=f[i]+f[i-1]        
        i=i+1
        
    return f

    
        