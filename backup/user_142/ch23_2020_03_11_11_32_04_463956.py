V = int(input('qual a velocidade?:'))
M = (V-80)*5
if V<=80:
	print('Não foi multado')
else:
	print('Voce foi multado no valor de {0:.2f}'.format(M))