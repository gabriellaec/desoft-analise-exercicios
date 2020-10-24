vel = int(input('Qual a velocidade do carro?: '))
if vel > 80:
    preco = (vel-80)*5 
    print('Você foi multado')
    print('{0:.2f}'.format(preco))
else:
    print('Não foi multado')