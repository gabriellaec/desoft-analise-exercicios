def classifica_idade:
    classifica_idade = input('Qual é a sua idade? ')
    	if classifica_idade <=11:
        	print('criança')
        if classifica_idade >=12 and classifica_idade <=17:
            print('adolescente')
        else:
            print('adulto')
print(str(classifica_idade))
    