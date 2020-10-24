def calcula_tempo(atletas):
    at_tempo = {}
    for k,v in atletas.items():
        tempo = (200/v)**0.5
        at_tempo[k]=tempo
    return at_tempo