a = input("Qual a distância que quer viajar?")
if a<=200 and a != 0:
	print ((a*0.5):.2f)
else:
	print ((40 +((a-200)*0.45)):.2f)    
