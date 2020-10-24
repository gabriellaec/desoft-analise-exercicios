x=int(input("Velocidade "))
	
def velocidade(x):    
	if x>80:
		return "Você foi multado em R$ {0:.2f}".format((x-80)*5)
	else:
		return "Não foi multado"