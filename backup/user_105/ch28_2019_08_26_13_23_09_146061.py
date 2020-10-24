velocidade = int(input('Qual a velocidade do carro: '))
if velocidade > 80:
    return (velocidade-80)*5
else:
    return ('não foi multado')
