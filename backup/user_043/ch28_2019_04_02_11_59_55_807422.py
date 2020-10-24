def multa_de_velocidade(velocidade):
    if velocidade>80:
        preço_multa=(velocidade-80)*5
    	return preço_multa
	else:
        return 'Não foi multado'
    
    