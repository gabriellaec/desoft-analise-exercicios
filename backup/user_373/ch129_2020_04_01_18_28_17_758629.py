def verifica_quadrado_perfeito(n):
    m=1
    while m<=n:
        n= n-1
        n= n+2
    if n==0:
        return True
    else:
        return False
    
    