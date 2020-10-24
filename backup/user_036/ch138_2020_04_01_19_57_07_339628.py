codigo = input('Código está executando? ')
while codigo != 's':
    print('Corrija o código e tente de novo')
    codigo = input('Código está executando? ')

resultado = input('Produz o resultado correto? ')
while resultado != 's':
    print('Corrija o código e tente de novo e volte para o começo de tudo')
    codigo = input('Código está executando? ')
    while codigo != 's':
        print('Corrija o código e tente de novo')
        codigo = input('Código está executando? ')
    resultado = input('Produz o resultado correto? ')
print('Parabéns!')