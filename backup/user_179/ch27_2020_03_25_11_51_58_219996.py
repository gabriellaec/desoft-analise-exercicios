tem_duvida = True
while tem_duvida:
	resposta = input ('Você está com dúvidas? ')
	if resposta == 'sim':
		print ("Pratique mais")
	else:
		print ("Até a próxima")
		tem_duvida = False