ano = int(input('Ano: '))
def eh_bissexto(Ano):
	if (ano%4==0 and ano%100!=0) or (ano%400==0):
    	print('True')
	else:
    	print('False')