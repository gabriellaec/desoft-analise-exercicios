def calcula_fibonacci(n):
    F=[0]*n
    if n==0:
        return []
    elif n==1:
        return [1]
    
        
    F[0]=1
    F[1]=1
    i=2
    while i<len(F):
        F[i]=F[i-1]+F[i-2]
        i+=1
    return F    
        