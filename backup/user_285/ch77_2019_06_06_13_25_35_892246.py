def calcula_tempo(atletas):
    tempo={}
    for corredor,aceleracao in atletas.items():
        vf=(200*aceleracao)**0.5
        t=vf/aceleracao
        tempo[corredor]=t
    return tempo