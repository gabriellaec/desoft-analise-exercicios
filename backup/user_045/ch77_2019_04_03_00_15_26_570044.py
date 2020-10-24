def calcula_tempo(n):
    d={}
    for nome,aceleracao in n.items():
        d[nome]=(200/aceleracao)**0.5
    return d
        