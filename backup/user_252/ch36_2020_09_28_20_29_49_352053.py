def fatorial(n):
    fat=1
    if n == 0:
        fat=1
        return fat
    else:
        i=1
        while i<=n:
            fat*=n
            i+=1
            n-=1
            return fat
            
            
            
            
       