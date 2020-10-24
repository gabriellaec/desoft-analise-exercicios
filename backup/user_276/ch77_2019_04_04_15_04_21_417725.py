def calcula_tempo(dicionario):
    output = {}
    for atletas, aceleracoes in dicionario.items():
        tempos_conclusao = (200/aceleracoes)**(1/2)
        output[atletas] = tempos_conclusao
    return output
        