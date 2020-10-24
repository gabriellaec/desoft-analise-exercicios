def multa(velocidade):
	if velocidade>80:
    	return'vc foi multado em {0} reais'.format (velocidade*5)
    else:
        return 'Não foi multado'
 print ((multa)(120))