def verifica_quadrado_perfeito(n):
    while n>0:
        i=1
        n-=i
        i+=2
    if n==0:
        return True
    else:
        return False