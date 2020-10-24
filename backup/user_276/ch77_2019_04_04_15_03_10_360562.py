def calcula_tempo(dicionario):
    output = {}
    for atletas, aceleracoes in dicionario.items():
        tempo_conclusao = (200/aceleracoes)**2
        output[atletas] = tempo_conclusao
    return output
        