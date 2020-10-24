idade = int(input('quala a sua idade '))
def classifica_idade(idade):
    if idade<11:
        print('crianca')
	elif 12<=idade<18:
        print('adolescente')
    else:
        print('adulto')