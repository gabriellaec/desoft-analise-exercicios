def segundos_entre(x,y):
    t=x[:2]
    u=x[3:5]
    z=x[6:8]
    p=y[:2]
    j=y[3:5]
    a=y[6:8]
    
    h1=int(t)
    m1=int(u)
    s1=int(z)
    h2=int(p)
    m2=int(j)
    s2=int(a)
    
    segundos1=(s1+(m1*60)+(h1*60*60))-(s2+(m2*60)+(h2*60*60))
    
    
    
    return segundos1