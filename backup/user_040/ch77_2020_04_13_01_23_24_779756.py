def calcula_tempo(x):
    dicionario = {}
    for atleta,aceleração in x.items():
        v2 = 2*aceleração*100
        t = v2**(1/2)/aceleração
        dicionario[atleta] = t
    return dicionario