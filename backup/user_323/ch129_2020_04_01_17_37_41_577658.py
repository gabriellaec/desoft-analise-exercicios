def verifica_quadrado_perfeito(n):
    x=1
    while n>0:
        n=n-x
        s+=2
    if n==0:
        return True
    if n<0:
        return False