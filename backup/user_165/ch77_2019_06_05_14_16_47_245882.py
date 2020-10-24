dicionario_atletas = {"Nome1": 1, "Nome2":2,"Nome3":1.5} 
def calcula_tempo(dicionario_atletas):
    dict = {}
    for atleta in dicionario_atletas:
        aceleracao = dicionario_atletas[atleta]
        tempo = (200*aceleracao)**0.5
        nomejogador = atleta
        dict[nomejogador] = tempo
    return dict
