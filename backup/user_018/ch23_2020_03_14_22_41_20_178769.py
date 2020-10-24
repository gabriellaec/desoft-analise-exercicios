v = int(input('Qual a velocidade?'))
if v>80:
	multa = (v - 80 )*5 
	print('Multa = {0:.2f}'.format(multa))
else: 
	print('Não foi multado')
              