def calcula_tempo(atletas):
    tempo={}
    for nome,aceleraçao in atletas.items():
        t=(200/aceleraçao)**0,5
        tempo [nome]=t
    return tempo