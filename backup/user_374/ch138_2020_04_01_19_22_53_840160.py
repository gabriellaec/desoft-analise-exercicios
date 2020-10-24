perg1 = input('Código está executando? ')

teste = True
while teste:
    if perg1 == 'n':
        print('Corrija o código e tente de novo')
        perg1 = input('Código está executando? ')
    else:
        perg2 = input('o código Produz o resultado correto? ')
        if perg2 == 'n':
                    print('Corrija o código e tente de novo e volte para o começo de tudo')
                    break
        elif perg2 == 's':
                    print('Parabéns!')
                    teste = False 
        