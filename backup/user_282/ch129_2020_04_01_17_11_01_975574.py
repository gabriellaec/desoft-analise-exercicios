def verifica_quadrado_perfeito(n):
    i = 1
    while n >= 0:
        if n == 0:
            return True
        n -= i
        i += 2
    else:  
        return False