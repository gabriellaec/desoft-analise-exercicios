while True:
    reposta1 = input('Código está executando?')
    if reposta1 == 'n':
        print('Corrija o código e tente de novo')
    if reposta1 == 's':
        reposta2 = input('O codigo está produzindo o resultado correto?')
        if reposta2 == 'n':
            print('Corrija o código e tente de novo e volte para o começo de tudo')
        elif reposta2 == 's':
            print('Parabéns!')
            break
            