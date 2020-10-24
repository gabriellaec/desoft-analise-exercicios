def calcula_tempo (atletas):
    tempo = {}
    for nome, a in atletas.items():
        t = 10/(a**(1/2))
        tempo[nome] = t
        return tempo  