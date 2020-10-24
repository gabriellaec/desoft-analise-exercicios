def verifica_idade(x):
    if 18>x<21:
        print('Liberado BRASIL')
    if x>21:
        print('Liberado EUA e BRASIL')
    else:
        print('Não está liberado')
	return verifica_idade