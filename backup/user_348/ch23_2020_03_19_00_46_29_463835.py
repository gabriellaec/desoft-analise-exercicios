velocidade = int(input('Qual a velocidade:'))
preço = velocidade*5.00
if velocidade > 80:
    print('A multa é {0}' .format(preço))
else:
    print('Não foi multado')
