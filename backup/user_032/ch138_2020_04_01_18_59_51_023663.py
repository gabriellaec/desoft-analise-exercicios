errado = True
while errado:
    pergunta = input('Código está executando?')
    if pergunta == 'n':
        print('Corrija o código e tente de novo')
    else:
        resultado_correto = input('O código produz o resultado correto?')
        if resultado_correto == 'n':
            print('Corrija o código e tente de novo e volte para o começo de tudo')
        else:
            print('Parabéns!')
            errado = False