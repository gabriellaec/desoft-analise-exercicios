velocidade = int(input('Qual a sua velocidade? '))

if velocidade > 80:
	multa = (velocidade - 80) * 5
    return 'Você foi multado com R$ ' + multa