distancia=int(input('qual a distancia a ser percorrida? '))
if distancia<=200:
	passagem=distancia*0.50
	print(round(passagem,2))
elif distancia>200:
	passagem2=passagem+(distancia-200)*0.45
	print(round(passagem,2))
