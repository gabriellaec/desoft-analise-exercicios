def eh_primo(numero):
    if numero < 2:
        return False
    contador = 2
    while contador < numero:
        if numero % contador == 0:
            return False
        contador += 1
    return True

def primos_entre(a, b):
    contador = 0
    p = a
    while p <= b:
        if eh_primo(p):
            contador += 1
        p += 1
    return contador