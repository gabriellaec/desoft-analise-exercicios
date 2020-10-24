def imprime_tipo(n):
    if n % 3 ==0 and n%5==0:
        return print('Tipo C')
    if n%3==0:
        return print('Tipo A')
    if n%5==0:
        return print('Tipo B')
    else:
        return print('Tipo D')
        