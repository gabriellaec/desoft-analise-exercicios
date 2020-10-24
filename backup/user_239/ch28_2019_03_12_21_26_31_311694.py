a=int(input('Velocidade do carro:'))

if a>80:
    y=(a-80)*5
    print ('Usuário levou multa de R${0:.2f}'.format(y))
else:
    print ('Não foi multado')
