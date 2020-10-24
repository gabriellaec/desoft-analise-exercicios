def calcula_fibonacci(n):
    f=[]
    i=0
    while i<n and i<2:
        f.append(1)
        i+=1
    while i<n:
        f.append([i-1]+[i-2])
        i+=1
    
        