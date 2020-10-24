def verifica_quadrado_perfeito (n):
    contador = 0
    while n> contador:
        n = n - (contador + 2)
        i = contador + 1
        if n == 0:
            return True
        elif n<0:
            return False
    