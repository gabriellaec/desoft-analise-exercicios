dicionario_atletas = {"Nome1": 1, "Nome2":2,"Nome3":1.5} 
def calcula_tempo(dicionario_atletas):
	for atleta in dicionario_atletas:
        aceleracao = dicionario[atleta]        
        tempo = (200*aceleracao)**0.5
        dicionario[atleta] = tempo
    return tempo 