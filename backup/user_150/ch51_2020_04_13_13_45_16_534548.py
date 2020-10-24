def eh_primo(numero):
    primopar = 2
    primeiroimpar = 3
    while numero % primopar != 0 and primeiroimpar < numero and numero % primeiroimpar !=0 and numero > 0 or numero == primopar or numero == 3:
        primeiroimpar += 2
        if primeiroimpar >= numero:
            return True
    return False

def primos_entre(a, b):
    primos = []
    x = a
    while x <= b:
        if eh_primo(x):
            primos.append(eh_primo(x))
        x += 1
    return primos