velocidade = float(input('Qual é a velocidade do seu carro em km/h: ')
if velocidade > 80:
    print ('Você foi multado')
    valor = (velocidade - 80)*5
    print ('O valor da multa foi de R${.:2f}'.format(valor))
else:
    print ('Não foi multado')