def descobre_senha():
	senha = 'desisto'
	chute = input('chute: ')
	while chute != senha:
		chute = input('chute: ')
	return "Você acertou a senha!"
    