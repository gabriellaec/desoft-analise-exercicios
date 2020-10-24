def imprime_tipo(numero):
    div3 = numero%3 == 0
    div5 = numero%5 == 0
    
    if div3 and not div5:
        print('Tipo A')
    elif div5 and not div3:
        print('Tipo B')
    elif div3 and div5:
        print('Tipo C')
    elif not div3 and not div5:
        print('Tipo D')