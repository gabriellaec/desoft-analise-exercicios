def calcula_tempo(atletas):
	dicio={}
	for nome,tempo in atletas.items():
		dicio[nome]=((200/tempo)**(1/2))
	return dicio
        
    