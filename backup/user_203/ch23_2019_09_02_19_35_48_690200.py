idade = input('Qual é a sua idade ? ')
def verifica_idade (idade):
	if idade < 18 :
		print ('Não está liberado')
	elif idade >= 21 :
		print ('Liberado EUA e BRASIL') 
	else: 
		print ('Liberado BRASIL') 
    