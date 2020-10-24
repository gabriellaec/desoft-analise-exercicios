def verifica_quadrado_perfeito(n):
    i=1
    while n-i==0:
        n=n-i
        i=i+2
    if n==0:
        return True
    else:
        return False   