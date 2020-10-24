def imprime_tipo(n):
    d3 = n%3 == 0
    d5 = n%5 == 0
    
    if d3 and not d5:
        print('Tipo A')
    elif d5 and not d3:
        print('Tipo B')
    elif d3 and d5:
        print('Tipo C')
    elif not d3 and not d5:
        print('Tipo D')