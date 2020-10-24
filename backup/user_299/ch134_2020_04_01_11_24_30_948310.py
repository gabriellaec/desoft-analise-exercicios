
def verifica_quadrado_perfeito (n,m):
    t=0
    pares = [2]*n
    while t<n:
        pares[t+1]=pares[t]+2
        t=t=1
    while m>=0:
        t=0
        m=m-pares[t]
        t=t+1
    if m*m == n:
        return True
    else:
        return False