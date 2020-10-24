def imprime_tipo(n):
    tipo = ''
    if n%3==0 and n%5!=0:
        tipo = 'Tipo A'
    if n%5==0 and n%3!=0:
        tipo = 'Tipo B'
    if n%3==0 and n%5==0:
        tipo = 'Tipo C'
    if n%3!=0 and n%5!=0:
        tipo = 'Tipo D'
    print(tipo)
    return tipo
