def verifica_quadrado_perfeito(n):
    while n>0:
        a = 1
        a = a + a + 2
        n = n - a
        if n == 0:
            return True
        elif n <0 :
            return False