def PiWallis(n):
    i=1
    cima=2
    baixo=1
    valor=2
    while i<n:
        if i%2!=0:
            baixo+=2
        if i%2==0:
            cima+=2
        valor=valor*(cima/baixo)
        i+=1
    return valor