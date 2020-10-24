def calcula_fibonacci(t):
    n=[1]*2
    i=2
    while i<t:
        n[i]=n[i-1]+n[i-2]
        i+=1
    return n
        
        