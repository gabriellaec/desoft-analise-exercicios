x=int(input("Velocidade "))
	
def velocidade(x):    
	if x>80:
		return "Você foi multado em ",(x-80)*5
	else:
		return "Não foi multado"