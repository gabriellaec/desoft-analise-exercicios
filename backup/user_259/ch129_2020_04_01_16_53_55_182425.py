def verifica_quadrado_perfeito(n):
    i = 1
    while True:
        n-=1
        if n>0:
            i+=2
        elif n == 0:
            return True
        elif n<0:
            return False