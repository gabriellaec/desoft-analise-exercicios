i = 1
def verifica_quadrado_perfeito(n):
    global i
    i = i + 2
    n = n - i**(n-2)
    if n == 0:
        return True
    elif n < 0:
        return False
print(verifica_quadrado_perfeito(25))
    