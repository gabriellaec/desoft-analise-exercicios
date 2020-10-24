def verifica_quadrado_perfeito(n):
    r=int(n**0.5)
    u=2*r
    for i in range(1,u,2):
        n=n-i
    if n==0:
        return(1<2)
    else:
        return(1>2)