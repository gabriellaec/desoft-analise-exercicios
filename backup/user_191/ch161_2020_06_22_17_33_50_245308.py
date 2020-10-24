def PiWallis(n):
    valor=[]
    t=2
    b=1
    while len(valor)<=n:
        valor.append(t/b)
        b+=2
        valor.append(t/b)
        t+=2
return(sum(valor)*2)