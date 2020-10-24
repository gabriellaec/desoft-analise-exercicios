def imprime_tipo(n):
    tipo = ''
    if n%3==0 and n%5!=0:
        tipo = 'Tipo A'
        print(tipo)
    if n%5==0 and n%3!=0:
        tipo = 'Tipo B'
        print(tipo)
    if n%3==0 and n%5==0:
        tipo = 'Tipo C'
        print(tipo)
    if n%3!=0 and n%5!=0:
        tipo = 'Tipo D'
        print(tipo)
    return tipo
