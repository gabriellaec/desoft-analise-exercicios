def PiWallis(n):
    den=1
    nom=2
    i=0
    resolucao=1
    while i<n:
        resolucao*=nom/den
        nom=den+1
        den=nom+1
        i+=1
    return resolucao*2