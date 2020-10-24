import math
def calcula_euler(x ,n):
    i=0
    t=2
    z=2
    somatoria = 0
    if n == 1:
        e = 1
    elif n == 2:
        e = 1 + x
    else:
        while i<n-2:
            somatoria = somatoria +(x**t)/math.factorial(z)
            t+=1
            z+=1       
            i+=1
            e = 1+x+somatoria
    return e
        
        
    