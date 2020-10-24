while True:
    perg1 = input('Código está executando?')
    if perg1 == 'n':
        print('Corrija o código e tente de novo')
        continue
    if perg1 == 's':
        perg2 = input('Produz o resultado correto?')
        if perg2 == 'n':
            print('Corrija o código e tente de novo')
        elif perg2 == 's':
            print('Parabéns!')
            break