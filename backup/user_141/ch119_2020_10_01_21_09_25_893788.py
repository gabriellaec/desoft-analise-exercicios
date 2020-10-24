def calcula_euler(x ,n):
    i=0
    t=2
    z=2
    f=2
    e=1+x
    while i<n:
        e = e + (x**t)/z*f
        t+=1
        z+=1
        f = (f*z+1)
        return e
        
        
    