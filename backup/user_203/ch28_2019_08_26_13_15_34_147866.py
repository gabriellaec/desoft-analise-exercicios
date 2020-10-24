Velocidade = int(input(' Digite a velocidade do seu carro'))
if Velocidade>80:
	x=5*(Velocidade-80)  
	print ('voce foi multado em {0:.2f}'.format(x))  
else: 
	print('voce nao foi multado')               