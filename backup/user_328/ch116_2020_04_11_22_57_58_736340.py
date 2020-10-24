def raiz_quadrada(numero):
    time = 0
    i=0
    x= True
    while i <= numero:
        numero -= i
        print('Valor do contador: ', i)
        if numero == 0:
            x = False
        i += 2
        time += 1
    return time