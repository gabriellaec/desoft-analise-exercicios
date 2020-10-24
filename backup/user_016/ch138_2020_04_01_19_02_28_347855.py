fluxograma = True
while fluxograma:
    pergunta1 = input('Código está executando? ')
    if pergunta1 == 'n':
        print('Corrija o código e tente de novo')
    elif pergunta1 == 's':
        pergunta2 = input('O código produz o resultado correto? ')
        if pergunta2 == 'n':
            print('Corrija o código e tente novamente')
        elif pergunta2 == 's':
            break
print('Parabéns!')