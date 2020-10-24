import math
def calcula_euler(x ,n):
    i=0
    t=1
    z=1
    
    somatoria = 0
    while i<n:
        somatoria = somatoria +(x**t)/math.fatorial(z)
        t+=1
        z+=1
       
        i+=1
    e = 1+x+somatoria
    return e
        
        
    