velocidade=float(input("qual sua velocidade?"))
if velocidade<=80:
	return None
else:
    multa=(velocidade-80)*5
    print("voce foi multado")
    print (multa)