def calcula_pi(n):
    i=0
    res=0
    while i<=n:
        res+=6/(i**2)
        i+=1
    resoficila=res**(0.5)
    return res