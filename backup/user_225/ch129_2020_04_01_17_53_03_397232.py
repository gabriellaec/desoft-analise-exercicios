def verifica_quadrado_perfeito(n):
    i = 1
    while n>0:
        n-=i
        i+=2
    if n == 0:
        return True
    elif n < 0:
        return False