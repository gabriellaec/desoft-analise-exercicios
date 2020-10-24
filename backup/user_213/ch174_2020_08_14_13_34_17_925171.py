def imprime_tipo(n):
    if n%3==0 and n%5!=0:
        return 'Tipo A'
    if n%5==0 and n%3!=0:
        return 'Tipo B'
    if n%3==0 and n%5==0:
        return 'Tipo C'
    if n%3!=0 and n%5!=0:
        return 'Tipo D'
