def verifica_quadrado_perfeito(n):
    x=1
    while True:
        n-=x
        x+=2
        if n == 0:
            return True
        if n<0:
            return False
            