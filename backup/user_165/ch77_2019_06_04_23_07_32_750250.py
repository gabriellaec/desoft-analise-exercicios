dicionario_atletas = {"Nome1": 1, "Nome2":2,"Nome3":1.5}
velocidade_inicial = 0 
def calcula_tempo(dicionario_atletas,velocidade_inicial):
	for atleta in dicionario_atletas:
        aceleracao = dicionario_atletas[atleta]
        tempo = (velocidade-velocidade_inicial)/aceleracao
    dicionario_atletas[atleta] = tempo
        