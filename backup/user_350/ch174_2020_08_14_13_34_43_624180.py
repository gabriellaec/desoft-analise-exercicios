def imprime_tipo(n):
    if n%3 == 0 and n%5 != 0:
        return 'Tipo A'
    elif n%5 == 0 and n%3 != 0:
        return 'Tipo B'
    elif n%3 == 0 and n%5 == 0:
        return 'Tipo C'
    elif n%3 != 0 and n%5 != 0:
        return 'Tipo D'