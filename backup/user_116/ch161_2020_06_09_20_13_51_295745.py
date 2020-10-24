def PiWallis(n):
    valor=1
    em_cima=2
    em_baixo=1
    for i in range(0,n):
        valor*=(em_cima/em_baixo)
        if i%2!=0:
            em_cima+=2
        else:
            em_baixo+=2
    return valor*2