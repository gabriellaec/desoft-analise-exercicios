def verifica_quadrado_perfeito(n):
    m=n
    while n>=0:
        i=1
        n-=i
        i+=2
    if n==0 and m!=1 and m!=3:
        return True
    else:
        return False