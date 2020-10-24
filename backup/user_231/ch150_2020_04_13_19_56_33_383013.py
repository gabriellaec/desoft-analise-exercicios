def calcula_pi(n):
    i=0
    i2=0
    d=[]
    d[0]=1
    while i<n-1:
        d.append(d+1)
        i+=1
    
    soma=(6/(d[i2])**2)
    while i2<n-1:
        soma = soma+(6/(d[i2]))
        i2+=1
    y=(soma)**1/2
    return y
    
    