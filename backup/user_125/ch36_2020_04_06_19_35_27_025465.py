def fatorial(n):   
    i=1
    for i in range(1,n):
        n*=i
        i+=1
    return n