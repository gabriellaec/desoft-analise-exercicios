def segundostotal(dias, horas, minutos, segundos):
	dias =input("Quantos dias?")
	horas =input("Quantas horas?")
	minutos =input("Quantos minutos")
	segundos =input("Quantos segundos?")
	y = segundos + minutos*60 + horas*3600 + dias*86400
	print (y)