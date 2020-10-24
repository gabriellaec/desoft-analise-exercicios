velocidade = int(input('Qual a velocidade do carro: '))
if velocidade > 80:
    velocidade_extra = velocidade-80
    multa = velocidade_extra*5
    print ('voce pagara {0:.2f}reais de multa: ').formal(multa)
else:
    print ('não foi multado')
