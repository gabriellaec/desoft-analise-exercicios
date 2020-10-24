a = 0
b = 0

while True:
    a = input('Código está executando?')
    if a == 'n':
        print('Corrija o código e tente de novo')
        continue

    elif a == 's':
        b = input('Produz o resultado correto?(n/s)')

        if b == 'n':
            print('Corrija o código e tente de novo e volte para o começo de tudo')
            continue
        
        else:
            print('Parabens!')
            break