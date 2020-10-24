def verifica_quadrado_perfeito(n):
    w=1
    while True:
        n-=w
        w+=2
        if n==0:
            return True
            break
        if n<0:
            return False
            break