def verifica_quadrado_perfeito(n):
    i=1
    if n==1:
        return True
    while i<=n:
        n-=i
        if n==0:
            return True
        elif n<0:
            return False
        i+=2