def eh_primo(numero):
    primopar = 2
    primeiroimpar = 3
    while numero % primopar != 0 and primeiroimpar < numero and numero % primeiroimpar !=0 and numero != 0 or numero == primopar or numero == 3:
        primeiroimpar += 2
        if primeiroimpar >= numero:
            return True
    return False

def maior_primo_menor_que(n):
    while not eh_primo(n):
        if n < 2:
            return -1
        else:
            n -= 1
    return n