def PiWallis(n):
    den=1
    nom=2
    i=0
    resolucao=1
    while i<n:
        resolucao*=nom/den
        if i%2==0:
            nom=nom
            den+=2
        else:
            nom+=2
            den=den
        i+=1
    return resolucao*2