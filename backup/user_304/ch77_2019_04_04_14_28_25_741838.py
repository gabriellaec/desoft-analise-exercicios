def calcula_tempo(atletas):
    tempo={}
    for nome,aceleraçao in atletas.items():
        a=int(aceleraçao)
        t=(200/a)**0,5
        tempo [nome]=t
    return tempo