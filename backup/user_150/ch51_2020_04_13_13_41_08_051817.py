def eh_primo(numero):
    primopar = 2
    primeiroimpar = 3
    while numero % primopar != 0 and primeiroimpar < numero and numero % primeiroimpar !=0 and numero != 0 or numero == primopar or numero == 3:
        primeiroimpar += 2
        if primeiroimpar >= numero:
            return True
    return False

def primos_entre(a, b):
    quantidade_de_primos = 0
    x = a
    while x <= b:
        if eh_primo(x):
            quantidade_de_primos += 1
        x += 1
    return quantidade_de_primos, eh_primo(x)