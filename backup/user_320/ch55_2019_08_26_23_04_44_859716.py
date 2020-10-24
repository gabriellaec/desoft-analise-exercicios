def eh_primo(numero):
    div = 0
    cont = 0
    if numero == 0 or numero == 1:
        return False
    while True:
        div += 1
        if numero % div == 0:
            cont += 1
        if div == numero:
            break
    if cont > 2:
        return False
    return True

def primos_entre(a, b):
    primos = []
    while b >= a:
        if eh_primo(b):
            primos.append(b)
        b -= 1
    return sorted(primos)