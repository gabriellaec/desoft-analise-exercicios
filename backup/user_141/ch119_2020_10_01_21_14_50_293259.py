def calcula_euler(x ,n):
    i=0
    t=2
    z=2
    f=2
    
    while i<n:
        somatoria = (x**t)/z*f
        t+=1
        z+=1
        f = (f*z+1)
        i+=1
    e = 1+x+somatoria
    return e
        
        
    