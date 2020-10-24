def verifica_quadrado_perfeito(n):
    s=1
    while n>0:
        n=n-s
        s+=2
    if n==0:
        return True
    if n<0:
        return False