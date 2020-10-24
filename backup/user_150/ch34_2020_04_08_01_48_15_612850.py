def eh_primo(numero):
    primopar = 2
    primeiroimpar = 3
    while numero % primopar != 0 and primeiroimpar < numero and numero % primeiroimpar !=0 and numero != 0 or numero == primopar or numero == 3:
        primeiroimpar += 2
        if primeiroimpar >= numero:
            return True
    return False

def avaliacao(n, z):
    if eh_primo(n) == False:
        ehprimo = eh_primo(n-z)
        ehprimo = True
        return ehprimo

def maior_primo_menor_que(n, z):
    while eh_primo(n) <= n:
        if eh_primo(n) == True:
            return eh_primo(n)
        elif eh_primo(n) == False:
            if n <= 1:
                return -1
            else:
                return avaliacao(n, z)