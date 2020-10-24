def verifica_quadrado_perfeito(n):
    v=1
    if n==1:
        return True
    while v<=n:
        n=v
        if n==0:
            return True
        elif n<0:
            return False
        v+=2