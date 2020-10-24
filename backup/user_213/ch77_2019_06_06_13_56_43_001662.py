def calcula_tempo(atletas):
    dici={}
    tempo=0
    for atleta,aceleracao in atletas.items():
        tempo = ((200*aceleracao)**1/2)/aceleracao
        dici[atleta] = tempo
    return dici
        
        
        