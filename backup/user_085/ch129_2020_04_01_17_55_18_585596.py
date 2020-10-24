def verifica_quadrado_perfeito(n):
    if n == 1:
        return True
    a = 1
    while n>=0:
        a = a + a + 2
        n = n - a
        if n == 0:
            return True
        elif n <0 :
            return False