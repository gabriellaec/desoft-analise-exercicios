def eh_primo(x):
    x=int(input('numero:'))
    while x>1:
        if x %2 == 0:
            return 'não é primo'
        else:
            return 'é primo'
        