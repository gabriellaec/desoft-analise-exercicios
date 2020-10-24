def raiz_quadrada(numero):
    tempo = 0
    i=0
    x= True
    while i <= numero:
        numero -= i
        print('Valor do contador: ', i)
        if numero == 0:
            x = False
        i += 2
        tempo += 1
    return tempo