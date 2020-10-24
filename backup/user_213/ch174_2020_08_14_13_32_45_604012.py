def imprime_tipo(n):
    if n%3==0 and n%5!=0:
        return 'Tipo A'
    if n%5==0 and n%5!=3:
        return 'Tipo B'
    if n%3==0 and n%5==0:
        return 'Tipo C'
    if n%3!=0 and n%5!=0:
        return 'Tipo A'
