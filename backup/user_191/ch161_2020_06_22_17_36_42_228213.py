def PiWallis(n):
    valor=0
    i=1
    t=2
    b=1
    if len(valor)<=n:
        valor=valor*append(t/b)
        b+=2
        if len(valor)<n:
            valor=valor*append(t/b)
            t+=2
    return(sum(valor)*2)