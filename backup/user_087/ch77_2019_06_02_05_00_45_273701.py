def calcula_tempo(dicionario_atletas):
    nome_tempo = dict()
    for nome in dicionario_atletas:
        tempo = (2*100/dicionario_atletas[nome])**(1/2)
		nome_tempo[nome] = tempo
    return nome_tempo
        