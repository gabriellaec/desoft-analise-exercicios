v = int(input("velocidade do carro"))

if v > 80:
    m = (v - 80) * 5
    print("sua multa foi {0}".format(round(m,2)))
else:
	print("Não foi multado")