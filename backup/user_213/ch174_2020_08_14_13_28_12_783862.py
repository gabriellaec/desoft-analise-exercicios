def imprime_tipo(n):
    if n%3==0 & n%5!=0:
        tipo = 'Tipo A'
    if n%5==0 & n%5!=3:
        tipo = 'Tipo B'
    if n%3==0 & n%5==0:
        tipo = 'Tipo C'
    if n%3!=0 & n%5!=0:
        tipo = 'Tipo A'
    return tipo