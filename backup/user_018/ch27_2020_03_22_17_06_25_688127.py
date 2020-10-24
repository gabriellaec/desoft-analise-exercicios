tem_duvidas = True
while tem_duvidas:
	resposta = input('Você tem dúvidas? ')
	if resposta != 'não':
		print('Pratique mais')
	else:
		print('Até a próxima.')
		tem_duvidas = False