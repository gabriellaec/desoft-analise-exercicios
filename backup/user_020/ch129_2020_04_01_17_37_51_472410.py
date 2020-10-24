i = 1
def verifica_quadrado_perfeito(n):
    global i
    i += 2
    if n == 1:
        n -= i**(n)
    else:
        n -= i**(n-2)
    if n == 0:
        return True
    elif n < 0:
        return False
print(verifica_quadrado_perfeito(1))
    