velocidade = int (input('Velocidade do carro:'))

if (velocidade > 80):
    print ('Por ultrapassar o limite de velocidade você foi multado em R$:{0:.2f}'.format((velocidade - 80)*5))
else:
    print ('Não foi multado')