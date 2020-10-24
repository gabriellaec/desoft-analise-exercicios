velocidade=int(input("qual sua velocidade?"))
multa=0
if velocidade>80:
    multa=(velocidade-80)*5
	print("{:.2f}".format(multa))
else: 
    print("Você n foi multado")