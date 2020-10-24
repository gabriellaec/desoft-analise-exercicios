velocidade = int(input('Digite a velocidade: '))

if velocidade > 80:
    print('Você foi multado! O valor da multa será de {0:.2f}'.format((velocidade-80)*5))
else:
    print('Não foi multado!')