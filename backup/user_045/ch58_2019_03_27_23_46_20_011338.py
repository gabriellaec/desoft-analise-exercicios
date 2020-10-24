def calcula_fibonacci(t):
    n=[]
    n[1]=1
    n[0]=1
    i=2
    while i<(t-1):
        n[i]=n[i-1]+n[i-2]
        i+=1
    return n
        
        