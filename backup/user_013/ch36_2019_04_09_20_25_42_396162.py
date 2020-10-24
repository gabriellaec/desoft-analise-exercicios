from math import sqrt
def eh_primo(n):
    if n <= 1:
        return False
    resultado = True
    for i in range(2,sqrt(n)):
        if n % i == 0:
            resultado = False
    return resultado