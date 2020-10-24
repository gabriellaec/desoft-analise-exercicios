distancia=int(input('qual a distancia a ser percorrida? '))
if distancia<=200:
	distancia*0.50=passagem
	print(round(passagem,2))
elif distancia>200:
    passagem+(distancia-200)*0.45=passagem2
    print(round(passagem,2))
