velocidade = int(input('Qual a sua velocidade? '))

if velocidade > 80:
	multa = (velocidade - 80) * 5
	print ('Sua multa foi de {:.2f}'.format(multa))
else:
    print ('Não foi multado')