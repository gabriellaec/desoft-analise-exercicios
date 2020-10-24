def lista_primos(numero):
    if numero == 0 or numero == 1:
        return False
    elif numero == 2:
        return True
    elif numero % 2 == 0:
        return False
    div = 3
    while numero > div:
        if numero % div == 0:
            return False
    return True
def lista_primos(n):
    contador = 1
        