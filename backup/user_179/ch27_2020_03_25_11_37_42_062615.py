resposta = True
while tem_duvida:
	resposta = input('Você ainda está com dúvidas? ')
    if resposta == 'sim':
        print ("Pratique mais")
	else:
		resposta = False
		print ("Até a próxima")