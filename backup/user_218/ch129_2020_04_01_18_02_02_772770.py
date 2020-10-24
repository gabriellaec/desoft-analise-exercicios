def verifica_quadrado_perfeito(n):
    a = 1
    while n >= a:
        n-=a
        a+=2
    if n == 0:
        return True
    if n < 0:
        return False