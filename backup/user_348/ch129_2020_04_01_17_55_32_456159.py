def verifica_quadrado_perfeito (n):
    i = 1
    while n>=i:
        n = n - (i + 2)
        i = i + 1
        if n == 0:
            return True
        elif n<0:
            return False
    