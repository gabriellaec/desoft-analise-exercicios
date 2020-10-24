def PiWallis(n):
    valor=0
    i=1
    t=2
    b=1
    if i<=n:
        valor=valor*append(t/b)
        b+=2
        i+=1
        if i<=n:
            valor=valor*append(t/b)
            t+=2
            i+=1
    return(sum(valor)*2)