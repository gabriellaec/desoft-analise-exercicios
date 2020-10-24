def eh_primo(numero):
    primopar = 2
    primeiroimpar = 3
    while numero % primopar != 0 and primeiroimpar < numero and numero % primeiroimpar !=0:
        primeiroimpar += 2
        return 'É primo!'
    else:
        return 'Não é primo!'