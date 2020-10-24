i = 1
def verifica_quadrado_perfeito(n):
    global i
    i += 2
    while n < i:
        n = n - i
    
        if n == 0:
            return True
        elif n < 0:
            return False