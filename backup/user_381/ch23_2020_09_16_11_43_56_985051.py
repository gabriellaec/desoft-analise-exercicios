x = int(input('Qual a velocidade do carro?'))
if x > 80:
    y = 5*(x - 80)
    print('Você foi multado')
    print(int('A multa é de {0:.2f}'.format(y)))
elif x <= 80: 
    y = 'Não foi multado'
